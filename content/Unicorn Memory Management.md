---
tags:
  - python
  - reverse_engineering
---
```python
from unicorn import *
from unicorn.x86_const import *
uc = Uc(UC_ARCH_X86, UC_MODE_32)

# allocate 16 bytes at 0x1000
uc.mem_map(0x1000,0x10)
uc.mem_write(0x1000, b"hello")
buf = uc.mem_read(0x1000, 0x10)
```