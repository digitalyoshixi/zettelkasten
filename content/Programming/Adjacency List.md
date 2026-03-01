---
tags:
  - programming
aliases:
  - AL
---
An [[C Arrays|Array]] that contains pointers to node [[Neighbourhood|Neighbourhoods]].
For a directed graph, this contains the out-
![[Drawing 2025-03-12 11.39.49.excalidraw]]
# Complexity
With $n = |V|$, $m = |E|$
- Adding an edge ($i,j$)
	- Worst Case : $O(1)$
- Remove edge ($i,j$)
	- Worst case: $O(n)$
- Edge query
	- Avg case $\Theta(deg(v))$
	- Worst case: $O(n)$
- Neighbour Query
	- Worst case: $O(1)$
- Adding node
	- Worst case: $O(n)$
- Deleting a node
	- Worst case $O(n^{2})$
- Space complexity: $\Theta(n+m)$