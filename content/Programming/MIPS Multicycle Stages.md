---
tags:
  - programming
---
![[MIPS Multicycle Stages-20250722150733654.webp]]
A revised form of [[Fetch Decode Execute]]
# Stages
### Instruction Fetch (IF)
- Gets the next 32-bit instruction, and increases PC
### Instruction Decode (ID)
- Decode the instruction
- Copy source registers into temporary A/B
### Execute
- Use [[Arithmetic Logic Unit|ALU]] to perform instruction
### MEM
- For lw, sw to access memory
- For use in branches to 
### WB
- Writes into [[Register File]]