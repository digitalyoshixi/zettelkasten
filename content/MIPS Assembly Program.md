---
tags:
  - assembly
---
The general structure of an assembly program should have:
- `.text` for all assembly code
- `.globl main` to make the main label visible to [[Operating System|OS]]
- `main:` to setup a main [[C labels|label]]
- [[Microprocessor Without Interlocked Pipelined Stages Assembly|MIPS Assembly Instructions]]
- [[Syscall]] at the end to signal program finish
![[MIPS Assembly Program-20250629165940859.webp]]
# Example Program
![[MIPS Assembly Program-20250629165955355.webp]]