---
tags:
  - programming
---
# Pseudocode
```
mark all verices white
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