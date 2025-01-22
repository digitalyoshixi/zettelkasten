---
tags:
  - python
  - c
---
Allows for copying a list so that the copy does not modify the original
# Python
```python
from copy import deepcopy
a = [1,2,3]
b = deepcopy(*a*)
```
Whenever you modify b, it will no longer change a
