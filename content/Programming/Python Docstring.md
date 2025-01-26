---
tags:
  - python
---
Documentation about the [[Python Function]].
Explains **what** the function does, not **how** it does it.
```python
def boom(bomb : list) -> *:
	"""
	returns and removes the final element of list bomb where len(bomb) > 0. 
	>>> boom([0,2,9,3])
	3
	>>> boom(["0s","cat","fish"])
	"fish"
	"""
	return bomb.pop()
```
# Anatomy
### Description
- Explain every parameter. Use parameter names
- Don't repeat type information
- Say pre-conditions for parameters (i.e ensure parameter 1 is non-negative)
- Don't say how the return value is computed
### Precondition
These are conditions about the parameters.
They can be anything BUT the parameter type.
### Example Cases
Write code that looks like a fake python interpreter.
# Testing
### Dictionary test
```python
"""
>>> mydict = {'a' : 20, 'b' : 21}
>>> mydict == myfunc(someinput)
True
"""
```