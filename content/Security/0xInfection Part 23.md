---
tags:
  - reverse_engineering
  - GDB
---
We are very familiar with gdb now. The process is as we know, gdb -q [filename], b _start, r, disas.

To step into, use si

To view registry information, use i r

To view value inside a buffer, use x/xb [buffer address]