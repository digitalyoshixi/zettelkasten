---
tags:
  - assembly
aliases:
  - Load Effective Address
---
`lea dest, src`
Used to store pointers to addresses in memory.
Moves the address of src into dest.
# Example
`lea rax, [rip+0x20040]`
- Will compute the address within the square brackets (Its not [[x86 Variable Dereferencing]])
- rax will then be that address