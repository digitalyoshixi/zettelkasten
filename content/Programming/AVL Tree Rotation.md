---
tags:
  - programming
  - datatype
---
A operation on an AVL tree that fixes rotations.
# Rotation Types
![[Drawing 2026-02-01 15.52.27.excalidraw]]
### Left Rotation
Done if [[AVL Balance Factor]] $> 1$
### Right Rotation
Done if [[AVL Balance Factor]] $< 1$
### Left-Right Rotation
Done if [[AVL Balance Factor]] $> 1$ and the left subtree [[AVL Balance Factor]] $< 1$
### Right-Left Rotation
Done if [[AVL Balance Factor]] $< 1$ and right subtree [[AVL Balance Factor]] $> 1$
# Code
```
if height(v.left) - height(v.right) > 1:
	let x = v.left
	if height(x.left) >= height(x.right):
		single left rotation: clockwise
	else:
		double left-right rotation: counter-clockwise then clockwise
else if height(v.right) - height(v.left) > 1:
	let x = v.right
	if height(x.left) <= height(x.right):
		single right rotation: counter-clockwise
	else:
		double right-left rotation: clockwise then counter-clockwise
else:
	no rotation
```