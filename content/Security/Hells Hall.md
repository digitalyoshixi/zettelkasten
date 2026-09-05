---
tags:
  - security
---
A revision of [[Indirect Syscall Evasion]].
Bypasses [[NTDLL]] hooks by jumping to a specific address in a linked [[Dynamic Linked Library|DLL]] consisting of a `syscall` beside a `ret` (Like a [[ROP Gadget]]).
# Jumper
```asm
mov r10, rcx # save first argument
mov eax, <ssn> # syscall number
jmp <address of 'syscall' gadget in NTDLL>
ret
```