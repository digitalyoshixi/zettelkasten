---
tags:
  - programming
---
# Algorithm
`insert(p, j): Inserts job with priority key p`
1. Insert at the end of the heap list
2. If it violates the heap order property ([[Max-Heap]], [[Min-Heap]]), swap with its parent ([[Bubble Up]])
# Max Heap Insert Pseudocode
```
insert(p,j):
	v := new_node(p,j)
	insert v at bottom-most level
	while v has parent p with p.priority < v.priority:
		swap v and p
		v's parent is changed
```