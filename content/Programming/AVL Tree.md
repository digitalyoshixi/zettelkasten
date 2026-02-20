---
tags:
  - programming
  - algorithm
aliases:
  - Adelson-Velskii-Landis Tree
---
A type of [[Self-Balancing Binary Search Tree]].
- Ensures a [[AVL Balance Factor]] $BF \in \{ -1, 0, 1 \}$ holds for every node in the tree
# Height
Finding height is a $O(\log n)$ operation.
$$
\text{minsize(h)} = \frac{\phi^{h+2}-(1-\phi)^{h+2}}{\sqrt{ 5 }}-1
$$
- With $\phi$ as [[Golden Ratio]]
- With $h$ as the height of the sub tree
# Operations
- [[AVL Tree Height]]
- [[AVL Tree Size]]
- [[AVL Tree Search]]
- [[AVL Tree Insert]]
- [[AVL Tree Delete]]
- [[AVL Tree Rotation]]
- [[AVL Tree Union]]
- [[AVL Tree Intersection]]
- [[AVL Tree Difference]]