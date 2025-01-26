---
tags:
  - python
  - programming
---
Regular python integers cannot accurately represent CPU bytes. Oftentimes, they may:
- wrap on an overflow
- truncate data
Python bitvectors are a better way of representing integers fitting wordsizes.
[[z3]] uses bitvectors for constraint finding
# Bitvector
![[Bitvector-20240714174955629.webp|429]]
Bitvector objects are integers. 
written in binary (or hex if you have imported `monkeyhex`).
# Attributes
### bv.length
Returns how wide the bitvector is in bits
# Bitvector <> Int Conversion
```python
bv = state.solver.BVV(0x1234, 32)       # create a 32-bit-wide bitvector with value 0x1234
<BV32 0x1234>                               # BVV stands for bitvector value

state.solver.eval(bv)                # convert to Python int
0x1234
```
