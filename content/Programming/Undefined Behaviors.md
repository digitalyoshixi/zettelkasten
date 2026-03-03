---
tags:
  - c
---
Any behavior that is not documented and may or may not crash the program if not handled well.
It is up to the compiler to determine if they want to implement some behavior or just let it lead to a crash.
# Uninitialized Variable
```c
int x;
printf("%d",x); // x given no value. compiler may crash
```
when variables are [[C Declarations|Declared]] but not defined, they get a garbage value from a segment of memory that they are set to.
# Examples
- [[Type Punning]]