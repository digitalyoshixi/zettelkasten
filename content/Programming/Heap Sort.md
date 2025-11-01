---
tags:
  - programming
aliases:
  - Max-Heap
---
A [[Heap]] where value of $i \leq$ value of parent.
![[Heap Sort-20251023161108185.webp]]
Often used as a [[Sorting Algorithms|Sorting Algorithm]]
# Algorithm
Assumes input is a unsorted array.
Uses algorithms:
- `build-max-heap` : create [[Heap Sort|Max-Heap]] from unsorted array
- `heapify` : create [[Heap Sort|Max-Heap]], assuming part of array is sorted
Algorithm is:
1. Create max heap with `build-max-heap`
2. Until list is sorted:
	1. Swap item at the start of heap list with item at end
	2. Run `heapify` to convert back to max-heap form