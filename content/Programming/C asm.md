---
tags:
  - programming
  - c
aliases:
  - C inline Assembly
---
Allows embedding of assembly instructions within C code.
```c
asm volatile ("mov %0, rsp")
```

# Macro Example
```c
#define GET_BP(bp) asm volatile ("mov %0, rbp" : "=r"(bp) : : );
// stores the rbp value into the variable given bp
```
