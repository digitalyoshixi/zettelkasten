---
tags:
  - programming
  - algorithm
aliases:
  - Prims Algorithm
---
A [[Greedy Algorithm|Greedy]] [[Data Structures and Algorithms|Algorithm]] to find [[Minimum Spanning Tree|MST]] by [[Breadth First Search|BFS]]
# Algorithm
- Create a [[Priority Queue|Minimum Priority Queue]] of visited nodes `visited[]`
	- Additional operation `decrease-priority(vertex, new-priority)`
- Pick an arbitrary node, add node to `visited`  list
- Look at all visit-able edges from nodes inside the visited list, add the minimum edge's node to the `visited` list if it is not already within the `visited` list
- priority(v) = minimum weight of any edge between v and tree
- priority(v) = inf if no such edge
# Complexity
- Vertex enter/leave min-heap: $O(\log n)$ each, $O(n \log n)$ full
- Edge call decrease-priority: $O(\log n)$ each for $O(m \log n)$ full
- Rest dont $\Theta(1)$ per vertex or edge
- Total worst case: $O((n+m)\log n)$