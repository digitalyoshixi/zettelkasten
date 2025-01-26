---
tags:
  - os
  - assembly
---
Very temporary storage for data often used for quick computations between variables. 

Register data is often saved into more permanent memory like the:
- [[Stack]]
- [[Heap]]
# Registers
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
