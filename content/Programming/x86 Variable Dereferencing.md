---
tags:
  - programming
  - assembly
---
```c
or [ebp-0x3], 0x8 // dereference the value of edp-0x3, and OR it with 0x8
mov eax, [ebx] // store 4 bytes at location ebx into eax
mov eax, [ebx+esi*4] // store 4 bytes at ebx+esi*4 into eax (allows for expressions within which is special)
```
Note that `[]` serve a different purpose in [[x86 lea|Load Effective Address]]
# Example With Malloc Fun
![[x86 Variable Dereferencing-20250830023919866.webp]]