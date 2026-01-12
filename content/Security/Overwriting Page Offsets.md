---
tags:
  - security
  - binary_exploitation
aliases:
  - Page Offset YOLO
---
A red-team tactic to bypass [[Address Space Layout Randomization|ASLR]].
- Everything in the program is relative to the base address
- Pages will always have a 0x1000 offset alignment.

![[Overwriting Page Offsets-20250207234449237.webp]]
This means the last 3 bytes of our address will never change.
Thus, we can just brute force until we find the base address and then continue our exploit as normal.
