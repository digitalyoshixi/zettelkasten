---
tags:
  - c
aliases:
  - Arithmetic Left Shift
  - Logical Left Shift
---
Moves all bits to the left.
This is a [[C Operators|Binary Operator]].
Both signed/unsigned operations are the same. The [[Least Significant Bit]] is replaced with 0.
```c
00101 << 1
= 01010
```
- A shift of a << n is equivalent to multiplying a \* 2^n