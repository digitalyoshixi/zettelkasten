---
tags:
  - programming
  - python
---
Used for enforcing behavior of functions defined by libraries.

# Example
```python
from __future__ import annotations
def foo(a: "str"): pass

print(foo.__annotations__)
```