---
tags:
  - debugging
  - reverse_engineering
---
The return address is the `$rsp` value before `leave`.
![[GDB View Return Address-20251120215832382.webp]]
```
pwndbg> x $rsp
0x7ffd157dedb8:	0x00005779e4ebe719
```