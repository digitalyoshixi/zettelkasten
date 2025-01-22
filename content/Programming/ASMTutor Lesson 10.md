---
tags:
  - x86
  - ASMTutor
---
### Lesson 10 Ascii printing to 10

Try printing an integer less than 32. You cannot using sys write, it will not print at all. Sys_write converts the decimal into the ascii character of itself, and any decimal below 32 is considered to be a control character. These control characters include: linefeed(ascii value 10), tab(ascii value 13), escape(ascii value 27), null(ascii value 0).

  

If we want to print numbers like 0,1,2,3,4… etc. then they will start at ascii 48.

For printing numbers in the double,triple,quadruple digits, then we will need to devise an algorithm for printing 2 conjugated digits side by side. The ascii for 10 is 4948 and not 58 as it would seem.