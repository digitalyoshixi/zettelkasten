---
tags:
  - programming
---
```
rank(S,k):
/*
Given key k, in set S, returns the rank
*/
	search(T,k) keep track of rank computed so far
	each move, add size of left subtree we skipped plus 1 for key itself
	if found key, add size n.left + 1 to rank
```