---
tags:
  - cpp
  - programming
aliases:
  - Float
---
Numerical values that hold decimal points can be [[Rational Number]] or [[Irrational Number]].
- float: 4 bytes
- double: 8 bytes
- long double: 8,12,16 bytes
Uses the `f` suffix in [[C++|CPP]]
# Floating point precision
Since, a decimal number can have infinite decimals, we cannot be able to store all digits.
- A float has 6 digits of lossless precision
- double values have 15 digits of lossless precision
- long double has at max 33 digits of lossless precision.

[[iomanip]] can alter the precision of your digits
# Scientific notation
`123.453e-7` and `0.123E3` are all valid.
every float is considered to be double, so the `e` notation serves for both float and double.
# Rounding Errors
Note that when floats are outputted, they are rounded. This is not true for the actual value of the float.
The actual value of the float will be its true value, so performing arithmetric operations will modify its true value aswell.
# Rounding Floats
```c
float a = 20.00000;

```