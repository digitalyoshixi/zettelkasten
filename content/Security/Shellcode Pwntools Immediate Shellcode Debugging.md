---
tags:
  - programming
  - security
---
```python
from pwn import *

gdb.debug_assembly("""
	mov eax, 60
	mov edi, 1337
	syscall
	int3
	nop
	nop
"""
)
```
You can use:
- `int3` to set breakpoints whenever you want