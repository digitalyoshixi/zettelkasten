---
tags:
  - python
  - math
---
```python
n = 5
r = 3
P = Permutations(range(n), r).list()
nPr = len(P)
print(f"Number of permutations P({n},{r}) = {nPr}")
```
Or:
```python
Permutations(range(n), r).cardinality()
```
Or:
```python
def Per(n,r):
	return factorial(n) / factorial(n - r)
```
