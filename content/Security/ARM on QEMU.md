---
tags:
  - assembly
  - ARM
---
QEMU is available to download on linux,mac and windows machines

We make a program using filename .s

Register 0 dictates standard output/input

To write to standard output, mov r0,#1

To write to standard input, mov r0,#0

To write to standard error, mov r0,#2

You can also use r0 to write to ANY file on the system. For example, create a txt file, then find its file identifier(its a integer), then have mov r0,#(file id)

  

To write a string:

1. r0 is the place to write to
    
2. r1 is the string
    
3. r2 is the length of the string
    
4. r7,#4 register the system interrupt to actually write to the r0 place
    
5. swi to software interrupt
    

In linux, system call 4 is actually the system call to write. Thus we have r7,#4

  

Once you save the program, to run it:

1. as [programname].s -o [programname].o
    
2. ld [programname].o -o [programname]
    
3. ./[programname]