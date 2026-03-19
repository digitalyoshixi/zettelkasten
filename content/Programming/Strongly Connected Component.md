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
# Definition
Consider definition of SCC: $S \subset V$ s.t $\forall v \in S, \forall u \in S, u \neq v \Rightarrow \exists \text{ path from } u \to v$
# Algorithms
- [[Kosaraju's Algorithm]]