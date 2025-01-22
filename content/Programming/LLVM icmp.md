---
tags:
  - llvm
---
### `icmp eq <datatype> <var1>, <datatype> <var2>`
Compares and returns a `i1` boolean representing of the two values are equal
```c
icmp eq i64 %d, 0
```
```c
icmp eq i64 %d, i64 %c 
```