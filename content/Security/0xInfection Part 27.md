---
tags:
  - 0xInfection
  - GDB
---
### Part 27 ASM hacking 2
The hack we are going to perform is one that takes advantage of registry values being editable. Usually we have mov %eax, %edx or some shit of sort. This value of %eax depends on value of %edx so if we edit edx, then eax will change when we step into.

The command we are going to use in the step before is “set $edx = 0x19”