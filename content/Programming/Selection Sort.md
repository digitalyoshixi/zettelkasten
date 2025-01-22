---
tags:
  - programming
---
Search through the list until you find the smallest item, then move that smallest item to the start of the list. That start of the list is now the sorted section, and anything not sorted is to the right.
![[Selection Sort-20241122210246398.webp]]
# Implementation
```python
for i in range(len(inputlist)):
	# find the index of smallest item
	index_of_smallest = inputlist.index(min(inputlist))
	L[index_of_smallest], L[i] = L[i], L[index_of_smallest]
```