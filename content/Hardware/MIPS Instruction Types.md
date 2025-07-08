---
tags:
  - hardware
  - programming
aliases:
  - R-Type
  - I-Type
  - J-Type
---
These are the assembly instruction types. Differentiated by what each collection of bits represents.
# R Type
![[MIPS Instruction Types-20250624153620609.webp]]
- `opcode` that is always $0$
- `rs` is a source register
- `rt` is a source register
- `rd` is the destination register that stores the result of the operation
- `shamt` is the shift ammount field, used only for shift operations
- `funct` specifies type of instruction performed (add, sub, and, etc) from [[MIPS Opcodes]]
# I Type
![[MIPS Instruction Types-20250624153632755.webp]]
- `opcode` : the opcode from [[MIPS Opcodes]]
- `rs` is a source register
- `rt` is the destination register
- `immediate` is a given value for various purposes. Two zeroes are  always at the end of the address
# J Type
![[MIPS Instruction Types-20250624153643874.webp]]
- `opcode` : the opcode from [[MIPS Opcodes]]
	- [[MIPS Jump]]
	- [[MIPS Jump and Link]]
- `address` : the address offset from current address to jump to. Two zeroes are always that the end of the address