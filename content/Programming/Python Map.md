---
tags:
  - python
---
A function for applying a [[Lambda Function]] over lists of iterables.
Directly modifies these values
```python
x = lambda a: a+2
map(x, [1,2,3,4], [4,3,2,1], ...)
```