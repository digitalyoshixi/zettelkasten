---
tags:
  - assembly
---
There are 32 registers in [[Microprocessor Without Interlocked Pipelined Stages|MIPS]].
![[MIPS Registers-20250629163213210.webp]]
# In [[Register File]]
### Value Storage
- `$t0 - $t9`: temporaries
- `$s0 - $s9`: saved temporaries
### Special
- `$zero`: will always hold 0. All writes will be discarded
- `$at`: reserved for the assembler
- `$gp`: global pointer
- `$sp`: stack pointer
- `$fp`: frame pointer (like [[rbp|Base Pointer]])
- `$ra`: return address
- `$k0, $k1`: reserved for the [[OS/Kernel|Kernel]]
### Function Parameters
- `$v0, $v1`: return values
- `$a0 - $a3`: function arguments
# Not in Register File
- `$PC` : [[Program Counter Register]]
- `$HI, $LO` : remainder and quotient respectively for division