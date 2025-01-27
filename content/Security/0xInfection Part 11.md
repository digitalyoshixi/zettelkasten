---
tags:
  - reverse_engineering
  - assembly
  - x86
---


### Part 11: Segment registers

Segment registers are used specifically for referencing memory locations. This is using the flat memory model of storing memory. Memory is split into segments like such:

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivae_tmp_d0962c503f299a02.png)

Focus on .data, .text and .stack.

.data is our data segment, .text is our code segment, .stack is our stack

There are 6 segment registers we can use to access these segments:

CS: code segment register. Stores base location of code section used for data access

DS: data segment register. Stores default location for variables used for data access

ES: extra segment register. Used during string operations

SS: stack segment register stores base location of stack segment. Used implicitly when accessing stack pointer(ESP) or base pointer(EBX)

FS: extra segment register

GS: extra segment register

Have you noticed? Every segment register is a pointer. They are auto-assigned at the start of the program and cannot be changed.

For the processor to retrieve instructions, it goes to the CS register, then adds the offset value in the EIP register according to the step it is on.

The DS, ES, FS and GS segment registers point to data segments. They help separate data elements and prevent overlap

The SS register is pointing to the stack segment. The stack contains data values passed to functions within the program. SS registers are considered part of the OS and cannot be read or changed in 99% of cases

  

When working in protected mode flat model(x86 architecture in 32bit), your program receives 4gb of address space that any 32bit register can freely play with EXCEPT, protected areas declared by the operating system.

  