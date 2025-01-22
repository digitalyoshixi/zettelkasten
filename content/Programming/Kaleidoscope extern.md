---
tags:
  - llvm
---
Behaves similar to [[Extern Variables]].
You can define a function before its use.
Beneficial for mutually-recursive functions.
```cpp
extern sin(arg);
extern cos(arg);
extern atan2(arg1 arg2);

atan2(sin(.4), cos(42))
```