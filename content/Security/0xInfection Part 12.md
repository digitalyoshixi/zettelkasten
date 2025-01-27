---
tags:
  - reverse_engineering
  - assembly
  - x86
---

### Part 12: instruction pointer register

The EIP register is the MOST important register in the WORLD! It keeps points to the next instruction to execute. After you jump to that pointer, it gets updated to the next.

We can hijack the EIP to change the flow of programs.

IA-32 architecture is intel 32bit architecture