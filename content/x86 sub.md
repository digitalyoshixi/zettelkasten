---
tags:
  - programming
  - x86
  - assembly
---
```
sub dest, val
```
Subtracts `val` from `dest`
- If `dest` < 0, then [[Carry Bit|Carry Flag]] is 1
- If `dest` = 0, then [[Zero Flag]] is 1