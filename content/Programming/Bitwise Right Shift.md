---
tags:
  - c
aliases:
  - Arithmetic Right Shift
  - Logical Right Shift
---
Moves all bits to right.
Bits that are lost are lost for good
```c
1011 >> 2 = 10
```
a >> n is equivalent to a * (1/2)^n
### Unsigned/Logical Shift
- The left bits are filled with zeros.
```c
1001 >> 1 = 0100
```
### Signed/Arithmetic Shift
- implementation defined
It can either:
1. Fill all with MSB
```c
101011 >> 2 = 111010 
```
2. Fill all with 0
```c
101011 >> 2 = 001010 
```
For positive values, a signed shift will be same as a unsigned shift.
