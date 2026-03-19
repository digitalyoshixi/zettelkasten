---
tags:
  - programming
aliases:
  - MST Cut Theorem
---
A theorem in [[Minimum Spanning Tree|MST]] that states for any [[Partition]] of a graphs vertices into two sets $(S, V-S)$ the edge with the minimum weight crossing this cut is part of the [[Minimum Spanning Tree|MST]].
# Theorem
- With [[Tree]] $T$ as a subtree of [[Minimum Spanning Tree|MST]] $T_{min}$
- With partitioning set of vertices $V$ into $(S, V-S)$ s.t:
	- No $T$ edge exists between $S$ and $V-S$
	- $(u,v)$ is the lightest edge connecting $V$, $V-S$
- Then, $T + \{ (u,v) \} \subset T_{min}$
