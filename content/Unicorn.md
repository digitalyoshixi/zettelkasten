---
tags:
  - virtualization
---
![[Unicorn-20250830175753193.webp|192]]
A multi-platform, multi-architecture CPU emulator framework.
- Based off [[QEMU]]
- Architecture-independent API
- Uses [[Just-in-time Compilation|JIT Compilation]], to allow for some code to be ran natively
- Implemented with C, and bindings for python. Code is executed in C, so all errors will be from the C program.
# Python Boilerplate
```python
from unicorn import *
from unicorn.x86_const import *
uc = Uc(UC_ARCH_X86, UC_MODE_32)
# setup stack
stack_base = 0x00100000
stack_size = 0x00100000
uc.mem_map(stack_base,stack_size)
uc.mem_write(stack_base,b'\x00' * stack_size)
uc.reg_write(UC_X86_REG_ESP, stack_base + stack_size//2) # set ESP to be the middle to allow for moving up or down (safety)

code = bytes.fromhex('b8 02 00 00 00 bb 03 00 00 00 03 c3')
target_base = 0x00400000
target_size = 0x00100000
uc.mem_map(target_base, target_size, UC_PROT_ALL)
uc.mem_write(target_base, b'\x00', target_size)
uc.mem_write(target_base, code)
# emu_start(start addr, end addr)
uc.emu_start(target_base, target_base+len(code), timeout=0, count=0)
print("done")
#code_start = uc.reg_read(UC_X86_REG_EIP)
#code = uc.mem_read(code_start, 0xc)
EAX = uc.reg_read(UC_X86_REG_EAX)
print(EAX) # 5

```
# Guides
- [[Unicorn Memory Management]]