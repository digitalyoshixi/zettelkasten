---
tags:
  - programming
---
A graph whose vertices can be divided into 2 independent sets $U, V$ such that every edge $(u,v)$ either connects to a vertex from $U$ to $V$, or a vertex from $V$ to $U$.
- No edge connects $V \to V$
- No edge connects $U \to U$
![[Bipartite Graph-20260301214652526.webp]]
- With $U$ as blue
- With $V$ as red
# Graph Detection Algorithm
Modified [[Breadth First Search|BFS]]:
- Start at random node, mark self as red
- While queue non-empty:
	- Mark neighbor visited, 
	- Mark colors
		- If red, mark neighbor blue
		- if blue, mark neighbor red
	- If neighbor is same color, terminate, graph is not bipartite
- If ended, then graph is bipartite