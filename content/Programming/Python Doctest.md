---
tags:
  - python
---
To test functions.
If a function is written using the [[Python Function Design Recipe]] and has `>>>` segments in the [[Python Docstring]], then doctest will test to see if the result of the command is the same as the result written.
# Using Doctest
```python
import doctest
doctest.testmod()
```
# Viewing All Outputs
```
python ./myfile.py -v
```
# Example Test
```python
def length(lst: list) -> int:
    """Return the number of elements (top level) in lst.
	>>> length([1,2,3]) 
	3
    """
    if (lst == []):
        return 0
    return 1 + length(lst[1:])
```