---
tags:
  - programming
---
Returns the maximum priority element of a [[Max-Heap]].
![[Heap Extract Max-20260301222950922.webp]]
# Algorithm
```
extract-max(heap)
```
- Removes the first element (max element) of the heap
- Make the right-most element of the list the first element
- Replace the first element with the left or right child (depending on if left > right or right > left) repeatedly given the heap property (bubble-down)
# Pseudocode
```
extract-max():
	max_p = root.priority
	max_j = root.job
	swap last/bottom/right-most node with the root
	remove the last node (the previous root)
	while root has child c with c.priority > root.priority:
		swap c and root
	return the max (that last node we removed)
```