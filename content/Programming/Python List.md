---
tags:
  - python
---
A collection of other objects that do not need to be the same datatype.
The are simply a range of pointers, that do not automatically update when the pointed-to value changes.
# <3.9 Lists
Before python 3.9, to make a list, you would need to use the [[Python typing]] library.
Lists are [[Polymorphic]]
```python
from typing import List
def get_total(values : List[int]) --> int:
	sum = 0
	for i in values:
		sum += i
	return sum
```
# Methods
- [[Python append]]
- [[Python extend]]
- [[Python List Addition]]
- [[Python Slicing]]
# Concepts
- [[Python List Comprehension]]