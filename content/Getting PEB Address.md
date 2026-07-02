---
tags:
  - windows
aliases:
---
# Assembly
```asm
mov rax, gx:[0x60]
```
# Visual Studio Macro
```c
DWORD peb = __readgsqword(0x60);
```
