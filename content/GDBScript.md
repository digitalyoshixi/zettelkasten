---
tags:
  - python
  - binary_exploitation
---
A python library for working with GDB only available through hooking GDB's interpreter
# Setup
Example file: `t.py`
```python
import gdb
print("hello")
```
Run with `gdb -q -x t.py`