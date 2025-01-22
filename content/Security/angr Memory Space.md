---
tags:
  - reverse_engineering
---
A byte-array of all memory addresses and their byte values as a python [[Bitvector]]
![[angr SimState-20240714174720083.webp]]
- Use array\[index] to specify a specific address
- use .\<type> to specify which [[Python Datatypes]] the memory should be interpreted as
# Modifying Memory
```python
state.mem[0x1000].long = 4
print(state.mem[0x1000].long.resolved) #<BV64 0x4>
```
# Attributes
### mem[addr].type.resolved
returns the memory value as a [[Bitvector]]
### mem[addr].type.concrete
returns the memory value as a python int