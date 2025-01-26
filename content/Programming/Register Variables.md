---
tags:
  - c
---
# Obsolete System
The C optimizer automatically creates register variables if it can.

# Register Variables
This variable will be heavily used.
They will be placed in machine registers, which result in smaller, faster programs.

```c
register int x;
```
registers can only be applied to [[Automatic Variables]]

# Very Restrictive
Register variables are very restrictive depending on the architecture.
Some may only allow `int`, `char` and `pointer` to be registers.