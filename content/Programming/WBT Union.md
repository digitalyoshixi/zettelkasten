---
tags:
  - programming
aliases:
  - WBT Join
---
Similar to [[AVL Tree Union]] except join is different.
You dont go all the way down the tree to locate key, you insert somewhere in the center of the tree.
# Algorithm
```pascal
join(L,k,G):
	if weight(L) > weight(G) * 3:
		p = L
		while weight(p.right) > weight(G) * 3:
			p = p.right
		q = new node(key=k, left=p.right, right=G)
		p.right = q
		rebalance and update sizes at p up to root
		return L
	elif weight(G) > weight(L) * 3:
		... symmetrical ...
	else:
		return new node(key=k, left=L, right=G)
```