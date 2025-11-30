---
tags:
  - blockchain
  - security
---
A [[Heap]] for the [[Ethereum Virtual Machine|EVM]].
- Consists of 32 [[Binary|Byte]] words.
# Structure
```
0x0 : 0x0000...0 (free space)
0x20 : 0x0000...0 (free space)
0x40 : 0x0000...80 (free stack pointer)
0x60 : 0x0000...0 (used as a index for dynamic arrays)
0x80 : 0x0000...0 (start f)
```
- [[Free Memory Pointer]] is always at `0x40` and points to the next available memory space