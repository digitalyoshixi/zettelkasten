---
tags:
  - programming
---
An operation performed in [[Heap]].
# Algorithms
- Check if the current node is the root node
- While heap property not satisfied:
	- Swap with parent
# Code
```cpp
void bubbleUp(MinHeap* heap, int nodeIndex){
  if (nodeIndex < 0 || nodeIndex >= heap->size) return;
  int curr_idx = nodeIndex;
  int parent_idx = get_parent(curr_idx1);
  while (heap->arr[curr_idx].priority < heap->arr[parent_idx].priority){
    swap(heap, curr_idx, parent_idx);
    curr_idx = parent_idx;
    parent_idx = get_parent(curr_idx);
  }
}
```
