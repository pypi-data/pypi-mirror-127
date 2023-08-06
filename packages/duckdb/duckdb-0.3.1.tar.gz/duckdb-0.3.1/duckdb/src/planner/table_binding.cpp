#include "duckdb/planner/table_binding.hpp"

#include "duckdb/common/string_util.hpp"
#include "duckdb/catalog/catalog_entry/table_catalog_entry.hpp"
#include "duckdb/catalog/catalog_entry/table_function_catalog_entry.hpp"
#include "duckdb/parser/expression/columnref_expression.hpp"
#include "duckdb/parser/tableref/subqueryref.hpp"
#include "duckdb/planner/bind_context.hpp"
#include "duckdb/planner/bound_query_node.hpp"
#include "duckdb/planner/expression/bound_columnref_expression.hpp"
#include "duckdb/planner/operator/logical_get.hpp"

namespace duckdb {

Binding::Binding(const string &alias, vector<LogicalType> coltypes, vector<string> colnames, idx_t index)
    : alias(alias), index(index), types(move(coltypes)), names(move(colnames)) {
	D_ASSERT(types.size() == names.size());
	for (idx_t i = 0; i < names.size(); i++) {
		auto &name = names[i];
		D_ASSERT(!name.empty());
		if (name_map.find(name) != name_map.end()) {
			throw BinderException("table \"%s\" has duplicate column name \"%s\"", alias, name);
		}
		name_map[name] = i;
	}
}

bool Binding::TryGetBindingIndex(const string &column_name, column_t &result) {
	auto entry = name_map.find(column_name);
	if (entry != name_map.end()) {
		result = entry->second;
		return true;
	}
	return false;
}

bool Binding::HasMatchingBinding(const string &column_name) {
	column_t result;
	return TryGetBindingIndex(column_name, result);
}

BindResult Binding::Bind(ColumnRefExpression &colref, idx_t depth) {
	column_t column_index;
	if (!TryGetBindingIndex(colref.column_name, column_index)) {
		return BindResult(StringUtil::Format("Values list \"%s\" does not have a column named \"%s\"", alias.c_str(),
		                                     colref.column_name.c_str()));
	}
	ColumnBinding binding;
	binding.table_index = index;
	binding.column_index = column_index;
	LogicalType sql_type = types[column_index];
	if (colref.alias.empty()) {
		colref.alias = names[column_index];
	}
	return BindResult(make_unique<BoundColumnRefExpression>(colref.GetName(), sql_type, binding, depth));
}

TableBinding::TableBinding(const string &alias, vector<LogicalType> types_p, vector<string> names_p, LogicalGet &get,
                           idx_t index, bool add_row_id)
    : Binding(alias, move(types_p), move(names_p), index), get(get) {
	if (add_row_id) {
		if (name_map.find("rowid") == name_map.end()) {
			name_map["rowid"] = COLUMN_IDENTIFIER_ROW_ID;
		}
	}
}

BindResult TableBinding::Bind(ColumnRefExpression &colref, idx_t depth) {
	column_t column_index;
	if (!TryGetBindingIndex(colref.column_name, column_index)) {
		return BindResult(StringUtil::Format("Table \"%s\" does not have a column named \"%s\"", colref.table_name,
		                                     colref.column_name));
	}
	// fetch the type of the column
	LogicalType col_type;
	if (column_index == COLUMN_IDENTIFIER_ROW_ID) {
		// row id: BIGINT type
		col_type = LogicalType::BIGINT;
	} else {
		// normal column: fetch type from base column
		col_type = types[column_index];
		if (colref.alias.empty()) {
			colref.alias = names[column_index];
		}
	}

	auto &column_ids = get.column_ids;
	// check if the entry already exists in the column list for the table
	ColumnBinding binding;

	binding.column_index = column_ids.size();
	for (idx_t i = 0; i < column_ids.size(); i++) {
		if (column_ids[i] == column_index) {
			binding.column_index = i;
			break;
		}
	}
	if (binding.column_index == column_ids.size()) {
		// column binding not found: add it to the list of bindings
		column_ids.push_back(column_index);
	}
	binding.table_index = index;
	return BindResult(make_unique<BoundColumnRefExpression>(colref.GetName(), col_type, binding, depth));
}

MacroBinding::MacroBinding(vector<LogicalType> types_p, vector<string> names_p, string macro_name_p)
    : Binding("0_macro_parameters", move(types_p), move(names_p), -1), macro_name(move(macro_name_p)) {
}

BindResult MacroBinding::Bind(ColumnRefExpression &colref, idx_t depth) {
	column_t column_index;
	if (!TryGetBindingIndex(colref.column_name, column_index)) {
		return BindResult(
		    StringUtil::Format("Macro \"%s\" does not have a parameter named \"%s\"", macro_name, colref.column_name));
	}
	ColumnBinding binding;
	binding.table_index = index;
	binding.column_index = column_index;

	// we are binding a parameter to create the macro, no arguments are supplied
	return BindResult(make_unique<BoundColumnRefExpression>(colref.GetName(), types[column_index], binding, depth));
}

unique_ptr<ParsedExpression> MacroBinding::ParamToArg(ColumnRefExpression &colref) {
	column_t column_index;
	if (!TryGetBindingIndex(colref.column_name, column_index)) {
		throw BinderException("Macro \"%s\" does not have a parameter named \"%s\"", macro_name, colref.column_name);
	}
	auto arg = arguments[column_index]->Copy();
	arg->alias = colref.alias;
	return arg;
}

} // namespace duckdb
