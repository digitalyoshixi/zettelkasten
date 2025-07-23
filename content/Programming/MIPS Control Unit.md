---
tags:
  - assembly
  - hardware
---
![[Microprocessor Without Interlocked Pipelined Stages-20250610200447957.webp]]
# Signals
### ALU
- ALU will always increment PC by 4
- ALUOp: Holds the next operation for the ALU to perform. Only passes part of the instruction (func part of [[MIPS Instruction Types|R-Type]] instructions, the rest is resolved from the instruction register)
- ALUSrcA: 1 bit signifying that the Input A into the ALU is:
	- Coming from PC(0)
	- Coming from register file(1)
- ALUSrcB: 2 bits signifying that input B is:
	- Coming from register file(0)
	- Coming from constant value(1)
	- Coming from instruction register(2)
	- Coming from shifted instruction register(3)
- RegWrite: A flag indicating if we are writing into the register file
- RegDST: Holds the destination address of our register write
![[MIPS Control Unit-20250722145947413.webp]]
### Instruction Register
![[MIPS Control Unit-20250722144706232.webp]]
- PCWrite: Writing the ALU output to PC
- PCWriteCond: Holds the ALU output and writes only if ALU's zero condition is true
- IorD: a flag determining if we are reading or writing
- IRWrite: The register data to be written
- PCSource: Holds the new value of PC
### Memory
- MemRead: A flag indicating the processor is reading from memory
- MemWrite: A flag indicating the processor is writing to memory
- MemToReg: A flag indicating the processor is recieving data from memory and not a register
