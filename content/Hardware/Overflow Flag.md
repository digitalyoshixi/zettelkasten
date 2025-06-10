---
tags:
  - cpp
---
This is  a [[CPU Flag|CPU Flag]] that indicates a addition/subtraction result overflows the wordsize.
# Logic
- For unsigned numbers, $C_{out} = 1$ indicates a overflow
- For signed numbers, $G=A+B$ overflow if and only if $A$ and $B$ have the same sign, but $G$ has the opposite sign
- For signed numbers, $G= A-B$ overflows if and only if $A$ and $B$ have a different sign and $G$ has the same sign as $B$