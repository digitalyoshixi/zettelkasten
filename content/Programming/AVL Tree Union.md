---
tags:
  - programming
aliases:
  - AVL Tree Split
  - AVL Tree Union
---
Given two [[AVL Tree]] $T_{1}, T_{2}$ the union of $T_{1}, T_{2}$ is a tree that contains the key-value pairs from $T_{1}$ and $T_{2}$
$$
(k, v_{1}) \in T_{1} \wedge (k, v_{2}) \in T_{2} \implies [(k,v_{1}) \in T \vee (k, v_{2}) \in T]
$$
# Complexity
$\Theta(n \log(\frac{m}{n}+1))$
- $n = \text{numnodes}(T_{1})$
- $m = \text{numnodes}(T_{2})$
# Algorithm 
Can be implemented with a [[Divide and Conquer]] algorithm
1. Split $T_{1}$ into smaller trees based off key
2. Split $T_{2}$ into smaller trees based off key
3. Build unions of smaller trees
4. Merge results into union of $T_{1}$ and $T_{2}$
```pascal
// returns a new tree pair, T1 is all elements less than k, T2 is all elements greater than k
split(T, k);
	if T == nil:
		return (nil, nil)
	if k == T.key:
		return (T.left, T.right)
	if k < T.key:
		(L,R) = split(T.left, k)
		R' = join(R, T.key, T.right)
		return (L, R')
	if k > T.key:
		(L, R) = split(T.right, k)
		L' = join(T.left, T.key, L)
		return (L', R)

// returns the union of tree L and G based off root k
join(L, k, G):
	if height(L) - height(G) > 1:
		p = L
		while height(p.right) - height(G) > 1:
			p = p.right
		q = new node(key=k, left=p.right, right=G)
		p.right = q
		rebalance and update heights at p up to root
		return L
	elif height(G) - height(L) > 1:
		...symmetrical..
	else:
		return new node(key=k, left=L, right=G)

union(T1, T2):
	if T1 == nil:
		return T2
	if T2 == nil:
		return T1
	k = T2.key
	(L,R) = split(T1, k)
	L' = union(L, T_2.left)
	R' = union(R, T_2.right)
	return join(L', k, R')
```