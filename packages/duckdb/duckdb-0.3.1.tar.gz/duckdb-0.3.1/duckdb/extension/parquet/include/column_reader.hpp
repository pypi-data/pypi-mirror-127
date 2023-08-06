//===----------------------------------------------------------------------===//
//                         DuckDB
//
// column_reader.hpp
//
//
//===----------------------------------------------------------------------===//

#pragma once

#include "parquet_types.h"
#include "thrift_tools.hpp"
#include "resizable_buffer.hpp"

#include "parquet_rle_bp_decoder.hpp"
#include "parquet_statistics.hpp"

#include "duckdb.hpp"
#ifndef DUCKDB_AMALGAMATION
#include "duckdb/storage/statistics/string_statistics.hpp"
#include "duckdb/storage/statistics/numeric_statistics.hpp"
#include "duckdb/common/types/vector.hpp"
#include "duckdb/common/types/string_type.hpp"
#include "duckdb/common/types/chunk_collection.hpp"
#include "duckdb/common/operator/cast_operators.hpp"
#include "duckdb/common/types/vector_cache.hpp"
#endif

namespace duckdb {
class ParquetReader;

using duckdb_apache::thrift::protocol::TProtocol;

using duckdb_parquet::format::ColumnChunk;
using duckdb_parquet::format::FieldRepetitionType;
using duckdb_parquet::format::PageHeader;
using duckdb_parquet::format::SchemaElement;
using duckdb_parquet::format::Type;

typedef std::bitset<STANDARD_VECTOR_SIZE> parquet_filter_t;

class ColumnReader {
public:
	static unique_ptr<ColumnReader> CreateReader(ParquetReader &reader, const LogicalType &type_p,
	                                             const SchemaElement &schema_p, idx_t schema_idx_p, idx_t max_define,
	                                             idx_t max_repeat);

	ColumnReader(ParquetReader &reader, LogicalType type_p, const SchemaElement &schema_p, idx_t file_idx_p,
	             idx_t max_define_p, idx_t max_repeat_p);

	virtual void InitializeRead(const std::vector<ColumnChunk> &columns, TProtocol &protocol_p) {
		D_ASSERT(file_idx < columns.size());
		chunk = &columns[file_idx];
		protocol = &protocol_p;
		D_ASSERT(chunk);
		D_ASSERT(chunk->__isset.meta_data);

		if (chunk->__isset.file_path) {
			throw std::runtime_error("Only inlined data files are supported (no references)");
		}

		// ugh. sometimes there is an extra offset for the dict. sometimes it's wrong.
		chunk_read_offset = chunk->meta_data.data_page_offset;
		if (chunk->meta_data.__isset.dictionary_page_offset && chunk->meta_data.dictionary_page_offset >= 4) {
			// this assumes the data pages follow the dict pages directly.
			chunk_read_offset = chunk->meta_data.dictionary_page_offset;
		}
		group_rows_available = chunk->meta_data.num_values;
	}
	virtual ~ColumnReader();

	virtual idx_t Read(uint64_t num_values, parquet_filter_t &filter, uint8_t *define_out, uint8_t *repeat_out,
	                   Vector &result_out);

	virtual void Skip(idx_t num_values);

	const LogicalType &Type() {
		return type;
	}

	const SchemaElement &Schema() {
		return schema;
	}

	virtual idx_t GroupRowsAvailable() {
		return group_rows_available;
	}

	unique_ptr<BaseStatistics> Stats(const std::vector<ColumnChunk> &columns) {
		if (Type().id() == LogicalTypeId::LIST || Type().id() == LogicalTypeId::STRUCT ||
		    Type().id() == LogicalTypeId::MAP) {
			return nullptr;
		}
		return ParquetTransformColumnStatistics(Schema(), Type(), columns[file_idx]);
	}

protected:
	// readers that use the default Read() need to implement those
	virtual void Plain(shared_ptr<ByteBuffer> plain_data, uint8_t *defines, idx_t num_values, parquet_filter_t &filter,
	                   idx_t result_offset, Vector &result) {
		throw NotImplementedException("Plain");
	}

	virtual void Dictionary(shared_ptr<ByteBuffer> dictionary_data, idx_t num_entries) {
		throw NotImplementedException("Dictionary");
	}

	virtual void Offsets(uint32_t *offsets, uint8_t *defines, idx_t num_values, parquet_filter_t &filter,
	                     idx_t result_offset, Vector &result) {
		throw NotImplementedException("Offsets");
	}

	// these are nops for most types, but not for strings
	virtual void DictReference(Vector &result) {
	}
	virtual void PlainReference(shared_ptr<ByteBuffer>, Vector &result) {
	}

	bool HasDefines() {
		return max_define > 0;
	}

	bool HasRepeats() {
		return max_repeat > 0;
	}

protected:
	const SchemaElement &schema;

	idx_t file_idx;
	idx_t max_define;
	idx_t max_repeat;

	ParquetReader &reader;
	LogicalType type;

private:
	void PrepareRead(parquet_filter_t &filter);
	void PreparePage(idx_t compressed_page_size, idx_t uncompressed_page_size);
	void PrepareDataPage(PageHeader &page_hdr);

	const duckdb_parquet::format::ColumnChunk *chunk;

	duckdb_apache::thrift::protocol::TProtocol *protocol;
	idx_t page_rows_available;
	idx_t group_rows_available;
	idx_t chunk_read_offset;

	shared_ptr<ResizeableBuffer> block;

	ResizeableBuffer offset_buffer;

	unique_ptr<RleBpDecoder> dict_decoder;
	unique_ptr<RleBpDecoder> defined_decoder;
	unique_ptr<RleBpDecoder> repeated_decoder;

	// dummies for Skip()
	parquet_filter_t none_filter;
	ResizeableBuffer dummy_define;
	ResizeableBuffer dummy_repeat;
};

} // namespace duckdb
