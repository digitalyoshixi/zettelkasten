---
tags:
  - programming
  - hardware
aliases:
  - PC
---
This is a [[Register]] that stores the location of the next instruction to fetch.
After every instruction fetch, PC is incremented by the wordsize of the processor.
# Incrementing PC
PC is incremented from the [[Arithmetic Logic Unit|ALU]].
![[Program Counter Register-20250624152612816.webp]]
# PC Requirements
- 4-bytes aligned
- MIPS can access any 8-byte memory from `0x00000000` to `0xffffffff`
- User memory limited to locations below `0x7fffffff`
- `.text` limited to locations below `0x00400000`
- `.data` limited to locations above `0x10010000`