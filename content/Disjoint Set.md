---
tags:
  - programming
aliases:
  - Union Find
---
A [[Data Structures and Algorithms|Data Structure]] representing a [[Set]] that can perform set operations. Created to solve the [[Dynamic Connectivity Problem]].
Often used in [[Kruskal's Algorithm|Kruskals Algorithm]]
# Operations
- `make-set(x)`: create a set that contains `x`
- `find-set(x)`: return the set that contains `x`
- `union(S1, S2)`: merge sets `S1` and `S2`
- `union(x1, x2)`: merge sets that  contains `x1` and `x2`
- `is-connected(x1,x2)`: check if `x1` and `x2` are in the same set
# Implementations
- [[Disjoint Set Linked List Implementation]]
- [[Disjoint Set Forest Implementation]]