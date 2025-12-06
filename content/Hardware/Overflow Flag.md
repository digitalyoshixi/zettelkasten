---
tags:
  - cpp
  - hardware
  - reverse_engineering
aliases:
  - OF
---
This is  a [[CPU Flag|CPU Flag]] that indicates a **signed** addition/subtraction result overflows the wordsize.
Different from [[Carry Bit|Carry Flag]]
# Logic
- For unsigned numbers, $C_{out} = 1$ indicates a overflow
- For signed numbers, $G=A+B$ overflow if and only if $A$ and $B$ have the same sign, but $G$ has the opposite sign
- For signed numbers, $G= A-B$ overflows if and only if $A$ and $B$ have a different sign and $G$ has the same sign as $B$