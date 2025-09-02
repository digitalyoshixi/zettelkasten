---
tags:
  - programming
  - assembly
  - x86
---
```
rep stosx
```
Used to initialize a buffer defined to start from `edi` to the value stored in `al`.
Often used with `xor eax, eax` to zero-out a whole buffer.
