---
tags:
  - security
---
A [[Position Independent Executable|PIE]] might have trouble with [[Trampoline Code|Trampoline]] functions as the [[Program Counter Register|PC]] position is changed.
To fix this, SBI tools will modify the program counter before any PC read.