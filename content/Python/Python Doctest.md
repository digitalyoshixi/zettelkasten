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