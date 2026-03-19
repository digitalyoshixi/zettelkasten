---
tags:
  - programming
---
An algorithm to find a [[Minimum Spanning Tree|MST]] from a [[Weighted Graph]]
# Algorithm
1. Keep finding the minimum edges that don't result in a [[Graph Cycle|Cycle]] for the MST
2. Do it again...
# Storing Cluster
1. Each cluster is a linked list
2. Merging two clusters is merging two linked lists
# Complexity
- $n = |V|, m = |E|$
- Collecting and storing edges $\Theta(m \log m)$
- Cluster updates (with [[Linked List]]) $O(\log n)$ per vertex, $O(n \log n)$ in total
- Total time is $O( (n+m) \log n)$