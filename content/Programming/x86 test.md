---
tags:
  - programming
  - x86
  - assembly
---
```
test dest, src
```
Equivalent to [[x86 and]], except it only modifies [[Zero Flag]].
# Testing Zeros
Used to check if a value is equal to 0:
```
test eax, eax
```
Sets [[Zero Flag|ZF]] to one if `eax` = 0.