---
tags:
  - reverse_engineering
---
map of all the state's [[Register]]
All registers are returned as a python [[Bitvector]]
# Modifying Registers
```python
state.regs.rsi = state.solver.BVV(3, 64) # set the rsi register to be 0x3 in 64 wordsize

print(state.regs.rsi) #<BV64 0x3>
```
