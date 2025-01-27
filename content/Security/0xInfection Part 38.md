---
tags:
  - reverse_engineering
  - GDB
---
### Part 38 more asm debugging tricks

“show variables” is how you view all memory addresses for variables

“disas” is incredibly useful for finding memory addresses of corresponding lines

“x/1c &variable” will show the value in a variable

To set the breakpoint to a memory address, you will type “b *address”

To remove the current breakpoint write “clear”

To go to first breakpoint, type “r” or “run”

To run in binary mode: gdb -q ./filename

To run in idk what mode: gdb -q filename