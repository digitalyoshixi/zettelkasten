---
tags:
  - programming
  - math
aliases:
  - SCC
---
These are maximal subsets of vertices reachable from each other in a directed graph.
![[Strongly Connected Component-20260212030202615.webp]]
$\{ e,o \}$, $\{ f,g,h,k \}$, $\{ m \}$
# Computing SCCs
1. [[Depth First Search|DFS]] on $G$
	1. Visit all vertices
	2. Store all finish times
	3. Accumulate verticies in reverse finish-time order
2. Compute [[Adjacency List]] of $G^{T}$
3. [[Depth First Search|DFS]] on $G^{T}$
	1. Use above order to pick start/restart vertices
4. Each tree found has vertices of one [[Strongly Connected Component]]

[[Computing Strongly Connected Component Proof]]