---
tags:
  - c
---
# Automatic Typecasting
The conversions that make sense are:
- int <-> char
- int <-> float
- int <-> bool
Automatic typecasting occurs in [[C Binary Operator Typecasting]]
# Explicit Typecasting
If you have 2 datatypes. `c` and `i`, an explicit typecast of `c = i` will:
- Make the right operand the same type as the left operand
- For high -> low(consult [[C Binary Operator Typecasting]]), excess high-order bits are discarded. 
- For low -> high, the value of the lower remains unchanged.
```c
int i;
char c;
i = c; // lower char -> higher int
c = i; // higher int -> lower char
```
### Coerced Typecasting
`(type-name) expression`
example is:
`(double) n`
# Custom Typecasts
- [[atoi()]]
- [[tolower()]]