---
tags:
  - programming
---
zn algorithm used to find [[Strongly Connected Component|SCC]]

https://invidious.yoshixi.net/watch?v=QlGuaHT1lzA
# Computing SCCs
1. [[Depth First Search|DFS]] on $G$
	1. Visit all vertices
	2. Store all finish times
	3. Accumulate node in reverse finish-time order (shortest finish time on top)
2. Compute [[Adjacency List]] of $G^{T}$
3. Setup a global visited list
4. For each node in the stack:
	1. [[Depth First Search|DFS]] on $G^{T}$ with that node, collecting visited nodes and adding to the global visited list aswell
	2. End of the road -> these visited nodes are a [[Strongly Connected Component|SCC]]
	3. Continue to next item in stack that is not visited before in the global visited list
# Proof
[[Computing Strongly Connected Component Proof]]
