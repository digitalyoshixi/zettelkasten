---
tags:
  - programming
aliases:
  - Weight Balanced BST
  - WBT
---
Keeping:
- $O(\log n)$ insert
- $O(\log n)$ search
- $O(\log n)$ delete
Requires some certain [[Weight Balance Factor]].
Can be used to implement [[Hashmap]]
# Balance
Tree is balanced if 
$$\frac{1}{3}\leq\frac{size(n.left)+1}{size(n.right)+1} \leq 3$$
$$\frac{1}{3}\leq\frac{weight(n.left)}{weight(n.right)} \leq 3$$
# Operations
- [[WBT Rotation]]