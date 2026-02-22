---
tags:
  - programming
aliases:
  - WBT Rebalance
  - WBT Rotation
---
# Case 1 - Right Heavy Tree
Assuming:
- WBT is right-heavy ($\text{weight}(v.\text{right}) > \text{weight}(v.\text{left}) \times 3$)
- $\text{weight(v.right.left)} < \text{weight(v.right.right)} \times 2$
balance by single counter-clockwise rotation.
![[Weight Balance Tree Rebalance-20260222032318596.webp]]
### Proof - Uses Diagram Above
1. Let $r = \text{size}(v.left)$
2. Let $s = \text{size}(v.right.left)$
3. Let $t = \text{size}(v.right.right)$
4. Suppose $s+1<2(t+1)$
5. Suppose $3(r+1) < s+t+2$
6. Consider cases:
	1. Case 1: node added to $v.right$ to cause imbalance
		1. Suppose before addition, we had a [[Weight Balanced Binary Search Tree|WBT]] $v$
		2. This means, $\frac{1}{3}*\text{weight}(v.right) \leq \text{weight}(v.left) \leq 3 *\text{weight}(v.right)$
		3. $\implies \frac{1}{3}(s+t+1) \leq r+1 \leq 3 (s+t+1)$
		4. Suppose before addition, we had a [[Weight Balanced Binary Search Tree|WBT]] $x$
		5. This means, $\frac{1}{3}*\text{weight}(x.right) \leq \text{weight}(x.left) \leq 3 *\text{weight}(x.right)$
		6. $\implies \frac{1}{3}(t) \leq s+1 \leq 3(t)$
		7. WTS: after addition, and rotation, we have a [[Weight Balanced Binary Search Tree|WBT]]
	2. Case 2: node removed from $v.left$ to cause imbalance
# Case 2 - Left Heavy Tree
When the [[Weight Balanced Binary Search Tree|WBT]] is left-heavy - single counter-clockwise rotation.