---
tags:
  - programming
  - security
---
![[Shellcode Bypass Forbidden Bytes Technique-20260121201923385.webp]]
For specific functions, certain bytes mean something special.

We can bypass this with certain techniques:
- [[Exclusive Or|XOR]]
- Move, and increment
- Move into different sizes of register
- Move and shift
- Make your shellcode is writable and increment data values in there
![[Shellcode Bypass Forbidden Bytes Technique-20260121202113943.webp]]
![[Shellcode Bypass Forbidden Bytes Technique-20260121202958035.webp]]