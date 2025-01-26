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
- rax will then take on the value of that address