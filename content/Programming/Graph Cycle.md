---
tags:
  - programming
aliases:
  - Simple Cycle
  - Cycle
---
A special type of [[Graph Path]] that results in the final node being the first node.
![[Graph Cycle-20250312153202556.webp|325]]
By convention, a cycle must contain atleast 3 different nodes
# Cycle Length
$\{ b,c,a,b \}$ : length 3
# Simple Cycle
A cycle wherein:
- Consecutive vertices are adjacent
- First vertex is last vertex
- Verticies are distinct except first and last which are the same (no repeats)
- $\langle v \rangle$ is not a cycle
# Detection
- [[DFS Cycle Detection]]