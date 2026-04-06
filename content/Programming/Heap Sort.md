---
tags:
  - programming
aliases:
---
A usage of [[Max-Heap]] as a [[Sorting Algorithms]]. 
# Algorithm
Assumes input is a unsorted array.
Uses algorithms:
- `build-max-heap` : create [[Max-Heap]] from unsorted array
- [[Heapify]] : create [[Max-Heap]], assuming part of array is sorted
Algorithm is:
1. Create max heap with `build-max-heap`
2. Until list is sorted:
	1. Swap item at the start of heap list with item at end
	2. Run `heapify` to convert back to max-heap form