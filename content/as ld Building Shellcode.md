---
tags:
  - programming
  - security
---
1. 
```
as -o shellcode.o shellcode.s
```
2. 
```
ld -o shellcode-elf shellcode.o
```
3. 
```
objcopy -dump-section .text=shellcode-raw shellcode-elf
```