---
tags:
  - programming
aliases:
  - Binary Heap
  - Nearly Complete Binary Tree
---
A [[Tree]] where all levels are mostly filled (except sometimes the lowest) starting from left to right.
Most often represented as a [[Binary Tree]], but does not require it.
Contains a heap property which is a relation of a node to its parent:
- `node` <= `parent` ([[Max-Heap]])
- `node` >= `parent` ([[Min-Heap]])
Implemented in memory with an [[Array]]
# Binary Heap
![[Heap-20260222205303684.webp]]
### Zero Indexed Language Parent/Children
- left = `2i + 1`
- right `2i + 2`
- parent `floor(i-1/2)`
# M-Ary Heap
### 1-Indexed
- k-th child: `m(i-1)+k+1`
- Parent: `floor( (m+i-2)/m )`
# Types
- [[Max-Heap]]
- [[Min-Heap|Min-Heap]]
# Operations
- [[Bubble Up]]
- [[Heapify]]
# Height
$Height = \log(n)+1$