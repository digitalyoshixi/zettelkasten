---
tags:
  - security
  - binary_exploitation
---
A method to bypass [[Data Execution Prevention|NX]] by using [[Just-in-time Compilation|JIT Compilation]] memory space (which is executable and writeable).
# Process
1. Make constants in code that will be JITed (`var evil = "%90%90%90%90%90%90"`)
2. JIT engine will `mprotect(PROT_WRITE)`, compile code into memory, then `mprotect(PROT_EXEC)`, code is now present in executable memory
3. Use a vulnerability to redirect execution into the constant
# Example
![[JIT Spraying-20260128023844400.webp]]
# JIT Spray Bypass ASLR
Compile alot of the same code, then hope you get lucky with the jmp
![[JIT Spraying-20260128024043952.webp]]