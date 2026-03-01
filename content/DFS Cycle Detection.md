---
tags:
  - programming
---
# Intuition
- For all nodes in the graph:
	- Try to visit all paths from that node, incrementing the visited list for each path, if the first node repeats then we have a cycle, backtrack after end-of-the road
# Pseudocode
```
mark all vertices white
for each vertex s:
	if s is white:
		if has-cycle(s): return True
	return False

has-cycle(u):
	mark u gray
	for each v in u's adjacency list:
		if v is white:
			predecessor(v) = u
			if has-cycle(v): return True
		elif v is gray and v is not predecessor(u):
			return True
	mark u black
	return False
```