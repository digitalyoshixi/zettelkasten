---
tags:
  - programming
  - x86
---
```
ret
```
Returns to the value of [[rip]] which is assumed to be at the top of the stack. And pops the top of the stack.
# Pseudocode
```
pop ecx
jmp ecx
```