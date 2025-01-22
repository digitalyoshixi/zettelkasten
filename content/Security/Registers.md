---
tags:
  - os
  - assembly
---
# 32-bit registers

| register | use-case                      |
| -------- | ----------------------------- |
| rax      | - math<br>- return values     |
| rbx      | - base index<br>- arrays      |
| rcx      | - counter                     |
| rdx      | - math                        |
| rbp      | - base pointer                |
| rsp      | - stack pointer               |
| rsi/rdi  | - memory transfer             |
| rip      | - current instruction pointer |

Very temporary storage for data. Usually used for quick computations between variables in processes like multiplication. Save the results into more permanent memory locations like RAM or cache.
### Registry sizes
[Registers - SkullSecurity](https://wiki.skullsecurity.org/index.php/Registers)

![[Registers-20240714174204220.webp]]
rax. rbx will act similarly to eax, ebx respectively. 
esi,edi,ebp,esp are either 32bit or 16bit. This is because memory addresses **cannot** be 8bit.

Example:
![[Registers-20240714174232040.webp]]
For some data types like [[ASCII]], all you need is 8 bits. Grabbing the entire register will just feed you extra garbage and halt execution time and RAM.
