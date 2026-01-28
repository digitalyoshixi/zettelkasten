---
tags:
  - programming
  - security
---
```python
from pwn import *

context.arch = 'amd64'

my_sc = asm("""
	mov eax, 60
	mov edi, 1337
	push 0x61
	syscall
""")
```