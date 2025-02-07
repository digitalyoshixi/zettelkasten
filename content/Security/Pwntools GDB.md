---
tags:
  - binary_exploitation
  - security
---
```python
from pwn import *
context.terminal = "kitty"

r = gdb.debug("./start")
r.send("AAAAAA")
```