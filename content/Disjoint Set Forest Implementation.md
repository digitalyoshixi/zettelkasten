---
tags:
  - programming
---
Using a [[Forest]] to create a [[Disjoint Set]]
![[Disjoint Set Forest Implementation-20260404221213019.webp]]
# Implementation
- Each set is a [[Tree]] where child leaves have pointers to parents
- The root node points to itself
- Each node stores a rank (upper bound on height of tree rooted at node)
### `make-set()`
Creates a single-node tree.
```perl
make-set():
	root := new node(value=x, rank = 0)
	root.parent := root
	return root
```
### `union(node1, node2)`
With `node1` present in one tree and `node2` present in another tree, makes the root of the shorter tree a child of the taller tree.
```perl
union(node1, node2):
	link(find-set(node1), find-set(node2))
link(root1, root2):
	if root1.rank > root2.rank:
		root2.parent := root1
	else:
		root1.parent := root2
		if root1.rank = root2.rank:
			root2.rank++	
```
### `find-set(node)`
```perl
find-set(node):
	if node.parent != node:
		return find-set(node.parent)
	return node
```
##### Path Compression Variant
Find-set will update the parent link directly to the root.
- Continue to go up parent until root node, assign parent to root
![[Disjoint Set Forest Implementation-20260405164905036.webp]]
# Complexity Analysis
- Best disjoint set implementation is forests
- Worse-case for $k$ operations with $n$ make-sets is $O(ka(n)) \in O(k \log^{*} n)$ 
	- $\log^{*}(n)$ is the number of times you need to apply log to $n$ until answer is $< 1$