---
tags:
  - programming
  - os
---
# Process
1. Setup the globals as assembly labels
2. Setup the [[Multiboot Standard|Multiboot Header]]
3. Setup the stack size
4. Setup the [[.text]] section with the start function `_start`
5. Set `esp` to point to stack top
6. Load [[Global Descriptor Table]]
7. Enable [[Paging]]
8. Enter high level kernel function `kernel_main`
9. Set self in infinite loop
# Code
https://wiki.osdev.org/Bare_Bones#Overview
```asm
.set ALIGN, 1<<0
.set MEMINFO, 1<<1
.set FLAGS, ALIGN | MEMINFO
.set MAGIC, 0x1BADB002
.set CHECKSUM, -(MAGIC+FLAGS)


.section .multiboot 
.align 4
.long MAGIC
.long FLAGS
.long CHECKSUM

.section .bss
.align 16
stack_bottom:
.skip 16384
stack_top:

.section .text
.global _start
.type _start, @function
_start:
  mov $stack_top, %esp
  call kernel_main
  cli
1:hlt
  jmp 1b
.size _start, . - _start
```