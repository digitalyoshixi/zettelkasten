---
tags:
  - programming
  - algorithm
aliases:
  - Prims Algorithm
---
A [[Greedy Algorithm|Greedy]] [[Data Structures and Algorithms|Algorithm]] to find [[Minimum Spanning Tree|MST]] by [[Breadth First Search|BFS]]
# Algorithm
- Create a [[Priority Queue|Minimum Priority Queue]] of nodes to visit `to_visit[]` Each node has:
	- A priority representing the shortest weighted edge connecting to the node
	- A parent representing parent of edge to this node
	- Queue has additional operation to change priority when-ever: `decrease-priority(vertex, new-priority)`
- AlSet all the priorities to elements in `to_visit[]`
- Pick an arbitrary node, add node to `to_visit[]` with 0 priority, no parent
- Look at all visit-able edges from nodes inside the visited list, add the minimum edge's node to the `visited` list if it is not already within the `visited` list
- priority(v) = minimum weight of any edge between v and tree
- priority(v) = inf if no such edge
# Pseudocode
```pascal
S := new container() for edges
PQ = new min-heap()
start := pick a vertex
PQ.insert(0, start)
for each vertex v != start: PQ.insert(v, inf)
while not PQ.is_empty():
	u := PQ.extract_min()
	S.add({u.pred, u})
	for each z in u's adjacency list:
		if z in PQ && weight(u,z) < priority of z:
			PQ.decrease_priority(z, weight(u,z))
			z.pred := u
return S
```
# Complexity
- Vertex enter/leave min-heap: $O(\log n)$ each, $O(n \log n)$ full
- Edge call decrease-priority: $O(\log n)$ each for $O(m \log n)$ full
- Rest dont $\Theta(1)$ per vertex or edge
- Total worst case: $O((n+m)\log n)$