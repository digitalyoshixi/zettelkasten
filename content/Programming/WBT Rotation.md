---
tags:
  - programming
---
![[Drawing 2026-02-02 09.25.17.excalidraw]]
# Left Rotation
- $\text{weight}(v.right) > 3 * \text{weight}(v.left)$
- $\text{weight}(v.right.left) < 2*\text{weight}(v.right.right)$
- [[WBT Left Rotation Proof]]
### Right Left Rotation
- $\text{weight}(v.right) > 3 * \text{weight}(v.left)$
- $\text{weight}(v.right.left) \geq 2*\text{weight}(v.right.right)$
# Right Rotation
- $\text{weight}(v.left) > 3 * \text{weight}(v.right)$
- $\text{weight}(v.left.right) < 2*\text{weight}(v.left.left)$
### Left Right Rotation
- $\text{weight}(v.left) > 3 * \text{weight}(v.right)$
- $\text{weight}(v.left.right) \geq 2*\text{weight}(v.left.left)$
$Weight(T) < Weight(S) \times 2$ is the sufficient condition for left rotating