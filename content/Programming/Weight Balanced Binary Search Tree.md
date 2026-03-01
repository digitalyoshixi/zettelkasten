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
# Weight
$$
weight(x) = size(x) + 1 = \text{\# of nodes}(x) + 1
$$
# Balance
Tree $n$ is balanced if 
$$\frac{1}{3}\leq\frac{size(n.left)+1}{size(n.right)+1} \leq 3$$
$$\frac{1}{3}\leq\frac{weight(n.left)}{weight(n.right)} \leq 3$$
# Height
$$
Height(T) \leq \frac{\log(weight(T))}{\log(\frac{4}{3})}
$$
Proof: [[WBT Height]]
# Operations
- [[Weight Balance Tree Rebalance]]
- [[WBT Rotation]]
- [[WBT Delete]]
- [[WBT Union]]