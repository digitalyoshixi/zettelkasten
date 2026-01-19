---
tags:
  - programming
  - algorithm
---
A type of [[Self-Balancing Binary Search Tree]]
Uses a [[Balance Factor]]
# Height
The height of the AVL Tree is the height of the left subtree minus the heght of the right subtree
$$
\text{minsize(h)} = \frac{\phi^{h+2}-(1-\phi)^{h+2}}{\sqrt{ 5 }}-1
$$
- With $\phi$ as [[Golden Ratio]]
- With $h$ as the height of the subtree
# Operations
### Insert
1. Find the node to become parent of the new node
2. Put new node in there
3. Rebalance and update heights if needed
Time complexity $O(\log n)$
### Delete
1. Find the node to delete $v$
	1. Case 1: V has no children: $O(1)$
	2. Case 2: V has one children: $O(1)$
	3. Case 3: V has two children: $O(\log n)$
		1. Find [[Successor Node]] $s$
		2. Find successor of $v$ with complexity 
		3. Move key vlaue pair of $s$ into $v$
		4. Delete $s$, s's parent adopts $s$ child child
