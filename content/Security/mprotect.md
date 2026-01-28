---
tags:
  - security
---
A [[Syscall]] to change the [[Data Execution Prevention|NX]] flags of a region of code
# Shellcode Bypass
1. Trick program into `mprotect(PROT_EXEC)`-ing our shellcode
2. Jump into the shellcode
We can do this with code reuse through [[Return Oriented Programming|ROP]]
