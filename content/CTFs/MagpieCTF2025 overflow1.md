---
tags:
  - binary_exploitation
  - ctf
---
1. strace to run and we find:
   ![[MagpieCTF2025 overflow1-20250223160956703.webp]]
2. Changing our inputs, we find that a string with length 47 will overflow the input
   ![[MagpieCTF2025 overflow1-20250223161212303.webp]]
3. Look at binary ninja, and find these hardcoded values in the memory
   ![[MagpieCTF2025 overflow1-20250223161748952.webp]]
```
cors33
aW5ub2NlbnQ=
```
1. The win condition is:
   ![[MagpieCTF2025 overflow1-20250223161914171.webp]]
2. With pwndbg, it simply checks if netrunner2d is within that segment
   ![[MagpieCTF2025 overflow1-20250223164000102.webp]]
3. With a cyclic pattern, we find that the offset is 37
   ![[MagpieCTF2025 overflow1-20250223164450954.webp]]
4. ![[MagpieCTF2025 overflow1-20250223164723909.webp]]