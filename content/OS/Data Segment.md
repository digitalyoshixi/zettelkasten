---
tags:
  - os
  - memory
---
A historical oddity.
With [[Address Space Layout Randomization|ASLR]], placed near-ish the PIE base
- Starts with size of 0
- Manged by [[brk()]] and [[sbrk()]] syscalls