---
tags:
  - math
  - programming
aliases:
  - Graph Transpose
  - Graph Transposition
---
The transpose of $G$ (Notation $G^{T}$) is a graph $G$ with:
- Same [[Graph Node|Vertices]] as $G$
- [[Graph Edge|Edge]] are reverses of $G$
![[Transposed Graph-20260212030450659.webp]]
# Transpose Algorithm
Time complexity: $O(n+m)$
```
allocate array T of size n
for i in 0,...,n-1:
	node = A[i]
	while node != null:
		T[node.id] = create_node(i)
		node = node->next
```