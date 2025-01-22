---
tags:
  - reverse_engineering
---
An object corresponding to a [[Basic Block]] of code found somewhere within the program.
![[angr Block-20240714172410065.webp]]
# Attributes
### block.instructions
Returns a integer value of how many instructions there are in the block
### block.instruction_addrs
Returns a array of all the addresses (in integer) of all instructions.
![[angr Block-20240714172526650.webp]]
### block.capstone
Returns the block in [[Capstone Disassembler]] format
### block.vex
Returns the block in [[angr Intermediate Representation]] which is [[VEX IR]] code
### block.entry_state()
Returns the entry [[angr SimState]]
# Methods
### block.pp()
Pretty-print of the disassembly to stdout
![[angr Block-20240714172455738.webp]]