---
tags:
  - assembly
aliases:
  - Load Effective Address
---
`lea dest, src`
Used to store pointers to addresses in memory.
Moves the address of src into dest.

Can also be used to compute values quickly, as it abuses `[]` feature to allow for computations rather than [[x86 Variable Dereferencing]].
# Example (Address)
`lea rax, [rip+0x20040]`
- Will compute the address within the square brackets (Its not [[x86 Variable Dereferencing]])
- rax will then be that address
- Equivalent to saying `mov rax, rip+0x20040` (but this instr is invalid)
# Example (Computation)
`lea rax, [rbx * 5 + 5]`
- With `rbx` storing a number instead of address
- `lea` is used for computations rather than address arithmetic
- More efficient for compiler