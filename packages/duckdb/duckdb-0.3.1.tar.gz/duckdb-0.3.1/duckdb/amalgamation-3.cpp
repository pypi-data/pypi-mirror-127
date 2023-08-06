#include "src/function/aggregate/distributive/kurtosis.cpp"

#include "src/function/aggregate/distributive/minmax.cpp"

#include "src/function/aggregate/distributive/product.cpp"

#include "src/function/aggregate/distributive/skew.cpp"

#include "src/function/aggregate/distributive/string_agg.cpp"

#include "src/function/aggregate/distributive/sum.cpp"

#include "src/function/aggregate/distributive_functions.cpp"

#include "src/function/aggregate/holistic/approximate_quantile.cpp"

#include "src/function/aggregate/holistic/mode.cpp"

#include "src/function/aggregate/holistic/quantile.cpp"

#include "src/function/aggregate/holistic/reservoir_quantile.cpp"

#include "src/function/aggregate/holistic_functions.cpp"

#include "src/function/aggregate/nested/histogram.cpp"

#include "src/function/aggregate/nested/list.cpp"

#include "src/function/aggregate/nested_functions.cpp"

#include "src/function/aggregate/regression/regr_avg.cpp"

#include "src/function/aggregate/regression/regr_count.cpp"

#include "src/function/aggregate/regression/regr_intercept.cpp"

#include "src/function/aggregate/regression/regr_r2.cpp"

#include "src/function/aggregate/regression/regr_slope.cpp"

#include "src/function/aggregate/regression/regr_sxx_syy.cpp"

#include "src/function/aggregate/regression/regr_sxy.cpp"

#include "src/function/aggregate/regression_functions.cpp"

#include "src/function/aggregate/sorted_aggregate_function.cpp"

#include "src/function/cast_rules.cpp"

#include "src/function/compression_config.cpp"

#include "src/function/function.cpp"

#include "src/function/macro_function.cpp"

#include "src/function/pragma/pragma_functions.cpp"

#include "src/function/pragma/pragma_queries.cpp"

#include "src/function/pragma_function.cpp"

#include "src/function/scalar/blob/base64.cpp"

#include "src/function/scalar/blob/encode.cpp"

#include "src/function/scalar/date/age.cpp"

#include "src/function/scalar/date/current.cpp"

#include "src/function/scalar/date/date_diff.cpp"

#include "src/function/scalar/date/date_part.cpp"

#include "src/function/scalar/date/date_sub.cpp"

#include "src/function/scalar/date/date_trunc.cpp"

#include "src/function/scalar/date/epoch.cpp"

#include "src/function/scalar/date/strftime.cpp"

#include "src/function/scalar/date/to_interval.cpp"

#include "src/function/scalar/date_functions.cpp"

#include "src/function/scalar/generic/alias.cpp"

#include "src/function/scalar/generic/constant_or_null.cpp"

#include "src/function/scalar/generic/current_setting.cpp"

#include "src/function/scalar/generic/least.cpp"

#include "src/function/scalar/generic/stats.cpp"

#include "src/function/scalar/generic/typeof.cpp"

#include "src/function/scalar/generic_functions.cpp"

#include "src/function/scalar/list/array_slice.cpp"

#include "src/function/scalar/list/list_concat.cpp"

#include "src/function/scalar/list/list_extract.cpp"

#include "src/function/scalar/list/list_value.cpp"

#include "src/function/scalar/list/range.cpp"

#include "src/function/scalar/map/cardinality.cpp"

#include "src/function/scalar/map/map.cpp"

#include "src/function/scalar/map/map_extract.cpp"

#include "src/function/scalar/math/numeric.cpp"

#include "src/function/scalar/math/random.cpp"

#include "src/function/scalar/math/setseed.cpp"

#include "src/function/scalar/math_functions.cpp"

#include "src/function/scalar/nested_functions.cpp"

#include "src/function/scalar/operators.cpp"

#include "src/function/scalar/operators/add.cpp"

#include "src/function/scalar/operators/arithmetic.cpp"

#include "src/function/scalar/operators/bitwise.cpp"

#include "src/function/scalar/operators/multiply.cpp"

#include "src/function/scalar/operators/subtract.cpp"

#include "src/function/scalar/pragma_functions.cpp"

#include "src/function/scalar/sequence/nextval.cpp"

#include "src/function/scalar/sequence_functions.cpp"

#include "src/function/scalar/string/ascii.cpp"

#include "src/function/scalar/string/caseconvert.cpp"

#include "src/function/scalar/string/chr.cpp"

#include "src/function/scalar/string/concat.cpp"

#include "src/function/scalar/string/contains.cpp"

#include "src/function/scalar/string/instr.cpp"

#include "src/function/scalar/string/jaccard.cpp"

#include "src/function/scalar/string/left_right.cpp"

#include "src/function/scalar/string/length.cpp"

#include "src/function/scalar/string/levenshtein.cpp"

#include "src/function/scalar/string/like.cpp"

#include "src/function/scalar/string/md5.cpp"

#include "src/function/scalar/string/mismatches.cpp"

#include "src/function/scalar/string/nfc_normalize.cpp"

#include "src/function/scalar/string/pad.cpp"

#include "src/function/scalar/string/prefix.cpp"

#include "src/function/scalar/string/printf.cpp"

#include "src/function/scalar/string/regexp.cpp"

#include "src/function/scalar/string/repeat.cpp"

#include "src/function/scalar/string/replace.cpp"

#include "src/function/scalar/string/reverse.cpp"

#include "src/function/scalar/string/string_split.cpp"

#include "src/function/scalar/string/strip_accents.cpp"

#include "src/function/scalar/string/substring.cpp"

#include "src/function/scalar/string/suffix.cpp"

#include "src/function/scalar/string/trim.cpp"

#include "src/function/scalar/string_functions.cpp"

#include "src/function/scalar/struct/struct_extract.cpp"

#include "src/function/scalar/struct/struct_pack.cpp"

#include "src/function/scalar/system/system_functions.cpp"

#include "src/function/scalar/trigonometrics_functions.cpp"

#include "src/function/scalar/uuid/gen_random.cpp"

#include "src/function/table/arrow.cpp"

#include "src/function/table/checkpoint.cpp"

#include "src/function/table/copy_csv.cpp"

#include "src/function/table/glob.cpp"

#include "src/function/table/pragma_detailed_profiling_output.cpp"

#include "src/function/table/pragma_last_profiling_output.cpp"

#include "src/function/table/range.cpp"

#include "src/function/table/read_csv.cpp"

#include "src/function/table/repeat.cpp"

#include "src/function/table/summary.cpp"

#include "src/function/table/system/duckdb_columns.cpp"

#include "src/function/table/system/duckdb_constraints.cpp"

#include "src/function/table/system/duckdb_dependencies.cpp"

#include "src/function/table/system/duckdb_indexes.cpp"

#include "src/function/table/system/duckdb_schemas.cpp"

#include "src/function/table/system/duckdb_sequences.cpp"

#include "src/function/table/system/duckdb_tables.cpp"

#include "src/function/table/system/duckdb_types.cpp"

#include "src/function/table/system/duckdb_views.cpp"

