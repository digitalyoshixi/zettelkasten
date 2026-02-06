---
tags:
  - programming
---
Changing the links of a [[Red-Black Tree|RBT]] without breaking the binary search tree property.
# Left Rotation
```python
def rotate_left(self, u):
	v = u.right
	u.right = v.left
	if v.left != self.nil:
		v.left.parent = u
	v.parent = u.parent
	if u.parent is None:
		self.root = v
	elif u.parent.left == u:
		u.parent.left = v
	else:
		u.parent.right = v
	v.left, u.parent = u, v
```