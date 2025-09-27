---
tags:
  - math
---
```python
C2 = Combinations(range(4),2)
C2.list()
C2.cardinality()
```
Or:
```python
Combinations(range(4),2).cardinality()
```
Or:
```python
def Com(n, r):
	return factorial(n) / ( factorial(r) * factorial(n-r) )
```
