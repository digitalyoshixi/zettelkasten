---
tags:
  - cpp
---
Occurs when you try and fit a larger value than the designated byte-size for a variable.
Value is lost, unintended behavior starts

# Unsigned Integer Modulo Wrap-around
For unsigned integers, it will change the value into a modulo wrap-around.
for example, the limit is 65535 for a unsigned short int. if given the value 65536, then the new value will be 1.

It can go the other way aswell.
Putting negative values for unsigned values will loop back to become a large positive value.
eg, -1 -> 65535

Because of this behavior, use of unsigned integers is ill-advised except for cases is bit manipulation or encryption