---
tags:
  - reverse_engineering
  - security
---
```python
from z3 import *
solver = Solver()
userinput = []
for i in range(4):
    userinput.append(BitVec(f'input{i}', 8)) # 8-bit char
solver.add(userinput[0] * 3 == 306)
solver.add(userinput[1] + userinput[2] == 160)
solver.add(userinput[1] * 3 == 324)
solver.add(userinput[3] - userinput[2] == 51)
solver.add(userinput[2] & userinput[3] == 0x24)
solver.add(userinput[2] << 1 == 104)
solver.add(userinput[0] + userinput[2] == 154)
solver.add(userinput[1] + userinput[3] == 211)
solver.add(userinput[0] ^ userinput[1] == 0x0a)
if solver.check() == sat:
    print("".join([chr(solver.model().eval(bv).as_long()) for bv in userinput]))
```