---
tags:
  - programming
  - datatype
---
A operation on an AVL tree that fixes rotations.
# Rotation Types
![[Drawing 2026-02-01 15.52.27.excalidraw]]
# Operation
1. Check if tree is left heavy or right heavy
2. Left heavy (Positive balance factor):
	1. Single rotate right
	2. Double rotate left, then right
3. Right heavy (Negative balance factor):
	1. Single rotate left
	2. Double rotate right then left
# Code
```
if height(v.left) - height(v.right) > 1:
	let x = v.left
	if height(x.left) >= height(x.right):
		single rotation: clockwise
	else:
		double rotation: counter-clockwise then clockwise
else if height(v.right) - height(v.left) > 1:
	let x = v.right
	if height(x.left) <= height(x.right):
		single rotation: counter-clockwise
	else:
		double rotation: clockwise then counter-clockwise
else:
	no rotation
```