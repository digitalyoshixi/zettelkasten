---
tags:
  - programming
  - python
---
A [[Python Object]] used to implement a [[Iterator Method]] with a given method to iterate to the next element.
Can only create iterators of [[Python Iterable]] objects.
# Class Definition
```python
class Iterable():
	def __iter__(self):
		pass
	def __next__(self):
		pass
```
# Creating Iterator
```python
mylist = ["Bob", "Joe", "Carl"]
myiterator = iter(mylist)
```