---
tags:
  - programming
aliases:
  - MST
---
A tree that covers all [[Graph Node|Vertices]] in a graph with minimal weight for its [[Graph Edge|Edge]].
# Formal Definition
A [[Tree]] $T$ s.t $\forall v \in V$ is an endpoint of atleast one edge in $T$ with minimum weights for edges used with $weight(T) = \sum_{(u,v)} \in T weight(u,v)$
# Alternate Definition
A subgraph of [[Programming/Graph|Graph]] $G$ that:
- Contains all vertices
- Is [[Graph Connected|Connected]]
- Has no [[Graph Cycle|Cycle]]
# Algorithms
- [[Kruskal's Algorithm]]