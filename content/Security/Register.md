---
tags:
  - os
  - assembly
---
A collection of [[Flip-Flop|Flip Flops]] within the [[Central Processing Unit|CPU]] used for very temporary storage of data used for quick computations, later saved within [[Stack]] or [[Heap]] variables. 
# Hardware Register
- [[Shift Register]]
- [[Load Register]]
# Software Registers
- [[rax]]
- [[rbx]]
- [[rcx]]
- [[rdx]]
- [[rbp]]
- [[rsp]]
- [[rsi]]
- [[rdi]]
- [[rip]]
### Registry sizes
[Registers - SkullSecurity](https://wiki.skullsecurity.org/index.php/Registers)
![[Registers-20240714174204220.webp]]
- `r__` means 64-bit
- `e__` means 32-bit
- `__` means 16-bit
- `_h`/`_l` means 8-bit, higher bits or lower bits respectively. Often used for [[ASCII]], where you only need 8-bits
Example:
![[Registers-20240714174232040.webp]]
