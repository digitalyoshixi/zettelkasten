---
tags:
  - programming
  - x86
  - assembly
---
```
push val
```
Sets the value at [[rsp]] to `val` and decrements [[rsp|esp]].
# Equivalence
```
sub esp, 4          ; Decrement stack pointer by 4 bytes (32-bit)
mov [esp], eax      ; Store eax at new top of stack
```