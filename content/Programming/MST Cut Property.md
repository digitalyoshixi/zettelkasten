---
tags:
  - programming
aliases:
  - MST Cut Theorem
---
A theorem for [[Minimum Spanning Tree|MST]] that states for any [[Partition]] of a graphs vertices into two sets $(S, V-S)$, the minimum weight crossing edge (a edge that connects a vertex in $S$ with another vertex in $V-S$) is part of the [[Minimum Spanning Tree|MST]].
![[MST Cut Property-20260418195121679.webp]]
![[MST Cut Property-20260418195735564.webp]]
# Theorem
- With [[Tree]] $T$ as a subtree of [[Minimum Spanning Tree|MST]] $T_{min}$
- With partitioning set of vertices $V$ into $(S, V-S)$ s.t:
	- No $T$ edge exists between $S$ and $V-S$
	- $(u,v)$ is the lightest edge connecting $V$, $V-S$
- Then, $T + \{ (u,v) \} \subset T_{min}$
