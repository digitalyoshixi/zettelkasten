---
tags:
  - programming
  - x86
  - assembly
---
```
pop dest
```
Sets `dest` to be the value of the first item of the stack, and then increment [[rsp|esp]]
# Equivalence
```
mov eax, [esp]      ; Load value from top of stack into eax
add esp, 4          ; Increment stack pointer by 4 bytes
```