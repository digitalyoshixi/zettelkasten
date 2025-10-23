---
tags:
  - programming
---
A [[Path Finding|Pathfinding]] algorithm for [[Weighted Graph|Weighted]] [[Directed Graph]] 
# Procedure
![[Bellman-Ford Algorithm-20251023163646477.webp|479]]
# Intuition
- We have a starting node at $s$
- We set a table of distances for all nodes, and initialize to $\infty$ distance for each
- For $\#(nodes)$ times, we run iterate through all nodes in the list
	- If the current node has a distance of $\infty$ skip it
	- If current node is $s$, or distance is not infinity, update distances of all outgoing edges