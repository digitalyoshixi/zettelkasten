---
tags:
  - c
  - memory
---
When only the pointers to the values are copied.
In cases like these, if passed, they will be considered pass by reference.
# Python
```python
import copy
x = 20
mycopy = copy.copy(x)
```