---
tags:
  - assembly
  - programming
  - x86
aliases:
  - x86
---
The assembly language that comes with [[CPU Labelling|x86]] processors.
- [[Endness|Little Endian]]
# Flavours
- [[x86 Assembly(Intel)]]
- [[x86 Assembly(AT&T)]]
# Concepts
- [[x86 CPU Flags]]
- [[Calling Convention]]
- [[x86 Globals]]
- [[x86 Variable Dereferencing]]
# Tools
- [[NASM]] is a popular assembler that can compile x86 code
# Boilerplate (Nasm)
```c
SECTION .data
msg     db      'Hello World!', 0Ah     ; assign msg variable with your message string
 
SECTION .text
global  _start
 
_start:
    mov     edx, 13     ; number of bytes to write - one for each letter plus 0Ah (line feed character)
    mov     ecx, msg    ; move the memory address of our message string into ecx
    mov     ebx, 1      ; write to the STDOUT file
    mov     eax, 4      ; invoke SYS_WRITE (kernel opcode 4)
    int     80h

```
# Boilerplate (as)
```c
.intel_syntax noprefix
.global _start
_start:
mov rax, 59
lea rdi, [rip+binsh]
mov rsi,0
mov rdx,0
syscall
binsh:
.string "/bin/sh"
```
