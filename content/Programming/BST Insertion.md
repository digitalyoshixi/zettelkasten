---
tags:
  - programming
---
# Process
1. To insert node $u$
2. If root node $v$ is less than $u$, then
	1. If root node has a left child, then the root $v$ is $v.left$
	2. Else, insert $u$ at v's left
3. If root node $v$ is more than $u$, then 
	1. If root node has a right child, then the root $v$ is $v.right$
	2. Else, insert $u$ at v's right