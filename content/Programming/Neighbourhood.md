---
tags:
  - programming
---
The nodes directly connected to the current node.
[[Graph Degree]] is the [[Set Cardinality]] of this neighbourhood.
# Definition
$\{ u | u \text{ is a neighbour/connected to } v \}$
# [[Directed Graph]]
![[Neighbourhood-20250312152947593.webp]]
### Out Neighbourhood
The list of nodes that the current node links to
In this case for node B, it is: `[C,D]`
### In Neighbourhood
The list of nodes that the current node is linked from
In this case for node B, it is: `[A]`
### Self-Linking Node
For a self-linking node, it is included within its neighbourhood set. Both in out neighborhood and in neighborhood.
# Auxilliary Concepts
- [[Graph Degree]]