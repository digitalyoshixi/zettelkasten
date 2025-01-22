---
tags:
  - assembly
  - ARM
  - GDB
---
Like most debuggers, we view things from steps.

1. break _start. This creates a breakpoint at the start of program
    
2. run
    
3. layout asm
    

To view register info, you can type: - info register r0

- layout regs

To continue steps, you can type: stepi

  

We can also examine inside a register. The values, if it is too big to be contained.

x/[number][display] $[register]

x/ is the examine key

[number] can be any digit like 10

[display] must be in a display for hex, decimal, character,etc. Can be: x,d,c

[register] will be a register like r1, r2, etc.

An example x/ can be: x/10d $r1