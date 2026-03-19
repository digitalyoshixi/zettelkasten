---
tags:
  - programming
---
A shortest [[Path Finding|Graph Traversal]] algorithm on a [[Programming/Graph|Graph]].
# Algorithm
- Given a [[Weighted Graph]]
- Given a list of all nodes
- Creating a empty list representing the distance from root node to each of the other nodes. Set all distances to infinity
![[Djikstra's Algorithm-20251023162944273.webp|327]]
Algorithm repeats until finished:
1. Visit all [[Neighbour]] nodes, and update the distance by adding current node distance and the weighted edge and comparing if its smaller than the current distance
![[Djikstra's Algorithm-20251023163222601.webp|321]]
2. Set current node to the neighbour with the smallest distance, and cross it out in unvisited node
![[Djikstra's Algorithm-20251023163240334.webp|325]]
# Pseudocode
```pascal
PQ := new min-heap()
PQ.insert(0, start) 
start.d := 0
// set all distances to inf
for each vertex v != start:
	PQ.insert(inf, v)
	v.d := inf
while not PQ.is-empty():
	u := PQ.extract-min()
	for each v in u's adjacency list, v in PQ:
		d' := u.d + weight(u,v)
		if d' < v.d:
			PQ.decrease-priority(v, d')
			v.d := d'
			v.pred := u
```
# Complexity
- $n = |V|$
- $m = |E|$
- Total time worst case $O( (n+m)\log n)$