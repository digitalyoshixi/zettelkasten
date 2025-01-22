---
tags:
  - 0xInfection
  - assembly
  - x86
---

### Part 13: Control registers:

There are 5 control registers which dictate the operating mode of the CPU and the characteristics of the currently executing task.

CR0: system flag that has control of OS and CPU states

CR1: reserved. Not currently implemented by intel. Why they decided to make CR2 and not finish CR1 is anybody’s guess.

CR2: memory page fault information

CR3: memory page directory information

CR4: flags that enable processor features and capabilities  
The values in each control register cannot be directly accessed however data in the control register can be moved to one of the general-purpose registers to be read. Changes to any control register can be done by modifying the general purpose register first, then moving that register into the control register.

Normal programs do not change the control register, however some do read it to determine flag values.