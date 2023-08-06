#include "duckdb/common/sort/sorted_block.hpp"

#include "duckdb/common/row_operations/row_operations.hpp"
#include "duckdb/common/sort/sort.hpp"
#include "duckdb/common/types/row_data_collection.hpp"

#include <numeric>

namespace duckdb {

SortedData::SortedData(const RowLayout &layout, BufferManager &buffer_manager, GlobalSortState &state)
    : layout(layout), block_idx(0), entry_idx(0), swizzled(false), buffer_manager(buffer_manager), state(state) {
}

idx_t SortedData::Count() {
	idx_t count = std::accumulate(data_blocks.begin(), data_blocks.end(), (idx_t)0,
	                              [](idx_t a, const RowDataBlock &b) { return a + b.count; });
	if (!layout.AllConstant() && state.external) {
		D_ASSERT(count == std::accumulate(heap_blocks.begin(), heap_blocks.end(), (idx_t)0,
		                                  [](idx_t a, const RowDataBlock &b) { return a + b.count; }));
	}
	return count;
}

void SortedData::Pin() {
	PinData();
	if (!layout.AllConstant() && state.external) {
		PinHeap();
	}
}

data_ptr_t SortedData::DataPtr() const {
	D_ASSERT(data_blocks[block_idx].block->Readers() != 0 &&
	         data_handle->handle->BlockId() == data_blocks[block_idx].block->BlockId());
	return data_ptr + entry_idx * layout.GetRowWidth();
}

data_ptr_t SortedData::HeapPtr() const {
	D_ASSERT(!layout.AllConstant() && state.external);
	D_ASSERT(heap_blocks[block_idx].block->Readers() != 0 &&
	         heap_handle->handle->BlockId() == heap_blocks[block_idx].block->BlockId());
	return heap_ptr + Load<idx_t>(DataPtr() + layout.GetHeapPointerOffset());
}

void SortedData::Advance(const bool &adv) {
	entry_idx += adv;
	if (entry_idx == data_blocks[block_idx].count) {
		block_idx++;
		entry_idx = 0;
		if (block_idx < data_blocks.size()) {
			Pin();
		}
	}
}

void SortedData::CreateBlock() {
	auto capacity =
	    MaxValue(((idx_t)Storage::BLOCK_SIZE + layout.GetRowWidth() - 1) / layout.GetRowWidth(), state.block_capacity);
	data_blocks.emplace_back(buffer_manager, capacity, layout.GetRowWidth());
	if (!layout.AllConstant() && state.external) {
		heap_blocks.emplace_back(buffer_manager, (idx_t)Storage::BLOCK_SIZE, 1);
		D_ASSERT(data_blocks.size() == heap_blocks.size());
	}
}

void SortedData::ResetIndices(idx_t block_idx_to, idx_t entry_idx_to) {
	block_idx = block_idx_to;
	entry_idx = entry_idx_to;
}

unique_ptr<SortedData> SortedData::CreateSlice(idx_t start_block_index, idx_t start_entry_index, idx_t end_block_index,
                                               idx_t end_entry_index) {
	// Add the corresponding blocks to the result
	auto result = make_unique<SortedData>(layout, buffer_manager, state);
	for (idx_t i = start_block_index; i <= end_block_index; i++) {
		result->data_blocks.push_back(data_blocks[i]);
		if (!layout.AllConstant() && state.external) {
			result->heap_blocks.push_back(heap_blocks[i]);
		}
	}
	// All of the blocks that come before block with idx = start_block_idx can be reset (other references exist)
	for (idx_t i = 0; i < start_block_index; i++) {
		data_blocks[i].block = nullptr;
		if (!layout.AllConstant() && state.external) {
			heap_blocks[i].block = nullptr;
		}
	}
	// Use start and end entry indices to set the boundaries
	result->entry_idx = start_entry_index;
	D_ASSERT(end_entry_index <= result->data_blocks.back().count);
	result->data_blocks.back().count = end_entry_index;
	if (!layout.AllConstant() && state.external) {
		result->heap_blocks.back().count = end_entry_index;
	}
	return result;
}

void SortedData::Unswizzle() {
	if (layout.AllConstant() || !swizzled) {
		return;
	}
	for (idx_t i = 0; i < data_blocks.size(); i++) {
		auto &data_block = data_blocks[i];
		auto &heap_block = heap_blocks[i];
		auto data_handle_p = buffer_manager.Pin(data_block.block);
		auto heap_handle_p = buffer_manager.Pin(heap_block.block);
		RowOperations::UnswizzleHeapPointer(layout, data_handle_p->Ptr(), heap_handle_p->Ptr(), data_block.count);
		RowOperations::UnswizzleColumns(layout, data_handle_p->Ptr(), data_block.count);
		state.heap_blocks.push_back(move(heap_block));
		state.pinned_blocks.push_back(move(heap_handle_p));
	}
	heap_blocks.clear();
}

void SortedData::PinData() {
	D_ASSERT(block_idx < data_blocks.size());
	auto &block = data_blocks[block_idx];
	if (!data_handle || data_handle->handle->BlockId() != block.block->BlockId()) {
		data_handle = buffer_manager.Pin(data_blocks[block_idx].block);
	}
	data_ptr = data_handle->Ptr();
}

void SortedData::PinHeap() {
	D_ASSERT(!layout.AllConstant() && state.external);
	auto &block = heap_blocks[block_idx];
	if (!heap_handle || heap_handle->handle->BlockId() != block.block->BlockId()) {
		heap_handle = buffer_manager.Pin(heap_blocks[block_idx].block);
	}
	heap_ptr = heap_handle->Ptr();
}

SortedBlock::SortedBlock(BufferManager &buffer_manager, GlobalSortState &state)
    : block_idx(0), entry_idx(0), buffer_manager(buffer_manager), state(state), sort_layout(state.sort_layout),
      payload_layout(state.payload_layout) {
	blob_sorting_data = make_unique<SortedData>(sort_layout.blob_layout, buffer_manager, state);
	payload_data = make_unique<SortedData>(payload_layout, buffer_manager, state);
}

idx_t SortedBlock::Count() const {
	idx_t count = std::accumulate(radix_sorting_data.begin(), radix_sorting_data.end(), 0,
	                              [](idx_t a, const RowDataBlock &b) { return a + b.count; });
	if (!sort_layout.all_constant) {
		D_ASSERT(count == blob_sorting_data->Count());
	}
	D_ASSERT(count == payload_data->Count());
	return count;
}

idx_t SortedBlock::Remaining() const {
	idx_t remaining = 0;
	if (block_idx < radix_sorting_data.size()) {
		remaining += radix_sorting_data[block_idx].count - entry_idx;
		for (idx_t i = block_idx + 1; i < radix_sorting_data.size(); i++) {
			remaining += radix_sorting_data[i].count;
		}
	}
	return remaining;
}

void SortedBlock::InitializeWrite() {
	CreateBlock();
	if (!sort_layout.all_constant) {
		blob_sorting_data->CreateBlock();
	}
	payload_data->CreateBlock();
}

void SortedBlock::CreateBlock() {
	auto capacity = MaxValue(((idx_t)Storage::BLOCK_SIZE + sort_layout.entry_size - 1) / sort_layout.entry_size,
	                         state.block_capacity);
	radix_sorting_data.emplace_back(buffer_manager, capacity, sort_layout.entry_size);
}

void SortedBlock::PinRadix(idx_t pin_block_idx) {
	D_ASSERT(pin_block_idx < radix_sorting_data.size());
	auto &block = radix_sorting_data[pin_block_idx];
	if (!radix_handle || radix_handle->handle->BlockId() != block.block->BlockId()) {
		radix_handle = buffer_manager.Pin(block.block);
	}
}

void SortedBlock::AppendSortedBlocks(vector<unique_ptr<SortedBlock>> &sorted_blocks) {
	D_ASSERT(Count() == 0);
	for (auto &sb : sorted_blocks) {
		for (auto &radix_block : sb->radix_sorting_data) {
			radix_sorting_data.push_back(move(radix_block));
		}
		if (!sort_layout.all_constant) {
			for (auto &blob_block : sb->blob_sorting_data->data_blocks) {
				blob_sorting_data->data_blocks.push_back(move(blob_block));
			}
			for (auto &heap_block : sb->blob_sorting_data->heap_blocks) {
				blob_sorting_data->heap_blocks.push_back(move(heap_block));
			}
		}
		for (auto &payload_data_block : sb->payload_data->data_blocks) {
			payload_data->data_blocks.push_back(move(payload_data_block));
		}
		if (!payload_data->layout.AllConstant()) {
			for (auto &payload_heap_block : sb->payload_data->heap_blocks) {
				payload_data->heap_blocks.push_back(move(payload_heap_block));
			}
		}
	}
}

void SortedBlock::GlobalToLocalIndex(const idx_t &global_idx, idx_t &local_block_index, idx_t &local_entry_index) {
	if (global_idx == Count()) {
		local_block_index = radix_sorting_data.size() - 1;
		local_entry_index = radix_sorting_data.back().count;
		return;
	}
	D_ASSERT(global_idx < Count());
	local_entry_index = global_idx;
	for (local_block_index = 0; local_block_index < radix_sorting_data.size(); local_block_index++) {
		const idx_t &block_count = radix_sorting_data[local_block_index].count;
		if (local_entry_index >= block_count) {
			local_entry_index -= block_count;
		} else {
			break;
		}
	}
	D_ASSERT(local_entry_index < radix_sorting_data[local_block_index].count);
}

unique_ptr<SortedBlock> SortedBlock::CreateSlice(const idx_t start, const idx_t end) {
	// Identify blocks/entry indices of this slice
	idx_t start_block_index;
	idx_t start_entry_index;
	GlobalToLocalIndex(start, start_block_index, start_entry_index);
	idx_t end_block_index;
	idx_t end_entry_index;
	GlobalToLocalIndex(end, end_block_index, end_entry_index);
	// Add the corresponding blocks to the result
	auto result = make_unique<SortedBlock>(buffer_manager, state);
	for (idx_t i = start_block_index; i <= end_block_index; i++) {
		result->radix_sorting_data.push_back(radix_sorting_data[i]);
	}
	// Reset all blocks that come before block with idx = start_block_idx (slice holds new reference)
	for (idx_t i = 0; i < start_block_index; i++) {
		radix_sorting_data[i].block = nullptr;
	}
	// Use start and end entry indices to set the boundaries
	result->entry_idx = start_entry_index;
	D_ASSERT(end_entry_index <= result->radix_sorting_data.back().count);
	result->radix_sorting_data.back().count = end_entry_index;
	// Same for the var size sorting data
	if (!sort_layout.all_constant) {
		result->blob_sorting_data =
		    blob_sorting_data->CreateSlice(start_block_index, start_entry_index, end_block_index, end_entry_index);
	}
	// And the payload data
	result->payload_data =
	    payload_data->CreateSlice(start_block_index, start_entry_index, end_block_index, end_entry_index);
	D_ASSERT(result->Remaining() == end - start);
	return result;
}

idx_t SortedBlock::HeapSize() const {
	idx_t result = 0;
	if (!sort_layout.all_constant) {
		for (auto &block : blob_sorting_data->heap_blocks) {
			result += block.capacity;
		}
	}
	if (!payload_layout.AllConstant()) {
		for (auto &block : payload_data->heap_blocks) {
			result += block.capacity;
		}
	}
	return result;
}

idx_t SortedBlock::SizeInBytes() const {
	idx_t bytes = 0;
	for (idx_t i = 0; i < radix_sorting_data.size(); i++) {
		bytes += radix_sorting_data[i].capacity * sort_layout.entry_size;
		if (!sort_layout.all_constant) {
			bytes += blob_sorting_data->data_blocks[i].capacity * sort_layout.blob_layout.GetRowWidth();
			bytes += blob_sorting_data->heap_blocks[i].capacity;
		}
		bytes += payload_data->data_blocks[i].capacity * payload_layout.GetRowWidth();
		if (!payload_layout.AllConstant()) {
			bytes += payload_data->heap_blocks[i].capacity;
		}
	}
	return bytes;
}

SortedDataScanner::SortedDataScanner(SortedData &sorted_data, GlobalSortState &global_sort_state)
    : sorted_data(sorted_data), total_count(sorted_data.Count()), global_sort_state(global_sort_state),
      total_scanned(0) {
}

void SortedDataScanner::Scan(DataChunk &chunk) {
	auto count = MinValue((idx_t)STANDARD_VECTOR_SIZE, total_count - total_scanned);
	if (count == 0) {
		D_ASSERT(sorted_data.block_idx == sorted_data.data_blocks.size());
		return;
	}
	// Eagerly delete references to blocks that we've passed
	for (idx_t i = 0; i < sorted_data.block_idx; i++) {
		sorted_data.data_blocks[i].block = nullptr;
	}
	const idx_t &row_width = sorted_data.layout.GetRowWidth();
	// Set up a batch of pointers to scan data from
	idx_t scanned = 0;
	auto data_pointers = FlatVector::GetData<data_ptr_t>(addresses);
	while (scanned < count) {
		sorted_data.Pin();
		auto &data_block = sorted_data.data_blocks[sorted_data.block_idx];
		idx_t next = MinValue(data_block.count - sorted_data.entry_idx, count - scanned);
		const data_ptr_t data_ptr = sorted_data.data_handle->Ptr() + sorted_data.entry_idx * row_width;
		// Set up the next pointers
		data_ptr_t row_ptr = data_ptr;
		for (idx_t i = 0; i < next; i++) {
			data_pointers[scanned + i] = row_ptr;
			row_ptr += row_width;
		}
		// Unswizzle the offsets back to pointers (if needed)
		if (!sorted_data.layout.AllConstant() && global_sort_state.external) {
			RowOperations::UnswizzleHeapPointer(sorted_data.layout, data_ptr, sorted_data.heap_handle->Ptr(), next);
			RowOperations::UnswizzleColumns(sorted_data.layout, data_ptr, next);
		}
		// Update state indices
		sorted_data.entry_idx += next;
		if (sorted_data.entry_idx == data_block.count) {
			sorted_data.block_idx++;
			sorted_data.entry_idx = 0;
		}
		scanned += next;
	}
	D_ASSERT(scanned == count);
	// Deserialize the payload data
	for (idx_t col_idx = 0; col_idx < sorted_data.layout.ColumnCount(); col_idx++) {
		const auto col_offset = sorted_data.layout.GetOffsets()[col_idx];
		RowOperations::Gather(addresses, FlatVector::INCREMENTAL_SELECTION_VECTOR, chunk.data[col_idx],
		                      FlatVector::INCREMENTAL_SELECTION_VECTOR, count, col_offset, col_idx);
	}
	chunk.SetCardinality(count);
	chunk.Verify();
	total_scanned += scanned;
}

} // namespace duckdb
