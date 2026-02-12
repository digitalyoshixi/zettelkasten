---
tags:
  - programming
aliases:
  - AM
---
An alternate way to represent adjacent edges.
It is also more space expensive.
![[Drawing 2025-03-12 11.45.37.excalidraw]]
# Undirected Graph
- Matrix would be symmetrical
- Diagonals would be 0
# Directed Graph
- Matrix is not symmetrical
- Diagonals do not necessarily need to be 0
# Complexity
With $n = |V|$, $m = |E|$
- Adding an edge ($i,j$)
	- Worst case : $O(1)$
- Remove edge ($i,j$)
	- Worst case: $O(1)$
- Edge Query
	- Worst case: $O(1)$
- Adding a node
	- Worst case: $O(n^{2})$
- Deleting a node
	- Worst case: $O(n)$
- Space complexity $\Theta(n^{2})$