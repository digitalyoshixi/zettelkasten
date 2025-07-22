---
tags:
  - hardware
---
A CPU that can allow for multiple cycles per operation.
Each instruction should be broken down into 3-5 [[Micro-Operation|Micro-Operations]]:
1. IF (Instruction Fetch)
2. ID (Instruction Decode)
3. Ex (Execute)
4. MEM (Memory)
5. WB (Write Back)

Often multicycle CPUs are [[Pipeline|Pipelined]]