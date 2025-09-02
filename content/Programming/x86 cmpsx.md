---
tags:
  - x86
  - assembly
  - programming
aliases:
  - x86 cmpsb
  - x86 cmpsw
  - x86 cmpsd
---
```
rep cmpsb
```
Used to check the buffers defined at `edi` and `esi` for differences.
Will continue until `ecx` is 0, or a difference is found.