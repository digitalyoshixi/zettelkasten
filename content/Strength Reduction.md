---
tags:
  - programming
  - compilers
aliases:
  - Bitwise Left Shift Optimization
---
Replacing expensive operations with cheaper operations:
- Replacing multiplication by a power of 2 with the corresponding left shift (`2x` -> `x << 1`)
- Replacing divisions with additions of shifts (`a/32767` -> `(a>>15) + (a>>30)`)