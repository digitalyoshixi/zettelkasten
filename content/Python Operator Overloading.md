---
tags:
  - programming
  - python
---
```python
class myownbool:
	def __init__(self, a):
		self.a = a
	# define behavior of '+'
	def __add__(self, o):
		return max(self.a, o.a)
```