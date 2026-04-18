---
tags:
  - programming
  - algorithm
aliases:
  - Prims Algorithm
---
A [[Greedy Algorithm|Greedy]] [[Data Structures and Algorithms|Algorithm]] to find [[Minimum Spanning Tree|MST]] by [[Breadth First Search|BFS]]
![[Prim's Algorithm-20260418215614589.webp]]
# Algorithm
- Create a empty MST list of edges
- Create a [[Priority Queue|Minimum Priority Queue]] of nodes to visit `to_visit[]` Each node has:
	- A priority representing the shortest weighted edge connecting to the node
	- A parent representing parent of edge to this node
	- Queue has additional operation to change priority when-ever: `decrease-priority(vertex, new-priority)`
- All all nodes of graph into `to_visit[]` with infinite priority
- Pick an arbitrary node, add node to `to_visit[]` with 0 priority, no parent
- While to `to_visit[]` queue is non-empty:
	- Extract the minimum element `u` of `to_visit`
	- If `u.parent` not null, add the edge `(u, u.parent)` to MST
	- Look at all visit-able edges:
		- If the edge has a smaller weight for the corresponding endpoint node `node` in `to_visit`, update that `to_visit[node]` to have this edge weight as priority and `u` as parent
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