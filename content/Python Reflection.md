---
tags:
  - programming
  - python
---
The ability to create a generalized object of a specific type.
Often done if empty parameters are passed to a specific datatype constructor.
# Example
```python
a = list() # reflection: creates empty list
b = dict() # reflection: creates empty dict
# Higher order example
def reverse(sequence):
	sequencetype = type(sequence)
	emptysequence = sequencetype() # reflection
	if sequence == emptysequence:
		return emptysequence
	else:
		# actual reverse logic here
```
