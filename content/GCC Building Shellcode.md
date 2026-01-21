---
tags:
  - programming
  - security
---
# Process
1. Write out shellcode as assembly
2. Assemble with 
```
gcc -wL,-N -nostdlib -static shellcode.s -o shellcode-elf
```
3. Extract shellcode 
```
objdump --dump-section .text=shellcode-raw shellcode-elf
```
# Example
```
.global _start
_start:
.intel_syntax_noprefix
	mov rax, 59
	lea rdi, [rip+binsh]
	mov rsi, 0
	mov rdx, 0
	syscall
binsh:
	.string "/bin/sh"
```
