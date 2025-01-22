---
tags:
  - llvm
---
### `select i1 <condition>, <datatype> <var>, <datatype> <var>`
```c
  %3 = select i1 %1, i64 -1, i64 %2
```
- The condition is in `i1` as its a boolean, it only needs one bit.
- If `%1` is true, then the value of `%3` is `-1`
- If `%1` is false, then the value of `%3` is `%2`