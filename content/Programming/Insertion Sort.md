---
tags:
  - programming
---
Iterates through the unsorted part and makes a sorted part, shifting the existing sorted copy every time a new value is found in the unsorted segment that comes before another sorted value.
![[Insertion Sort-20241122211007603.webp]]
# Python Implementation
```python
def insertionsort(L) -> None:
	for i in range(len(L))
		value = L[i]
		j = i
		while j != 0 and L[j - a] > value:
			L[j] = L[j-1]
			j=j-1
		L[j] = value
```
