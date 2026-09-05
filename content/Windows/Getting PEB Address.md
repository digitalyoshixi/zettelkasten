---
tags:
  - windows
aliases:
---
# Assembly
```asm
mov rax, gs:[0x60]
```
Or
```asm
mov rax, gs:[0x30]    ; Loads from NT_TIB the pointer "Self" (linear address of TEB)
mov rax, [rax + 0x60] ; Adds offset 0x60 to this address and loads PEB
```
# Visual Studio Macro
```c
DWORD peb = __readgsqword(0x60);
```
