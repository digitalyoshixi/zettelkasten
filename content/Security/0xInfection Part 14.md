---
tags:
  - 0xInfection
  - assembly
  - x86
---

### Part 14: Flags:

This is one of the most difficult concepts to grasp in assembly. Flags help control, check and verify program execution. They are instrumental in making sure each operation is done and done right.

There are 3 kinds of flags. Status flags, control flags and system flags.

  

Status flags:

CF: Carry flag. When the unsigned result of a math operation is too big to be stored within the word size. Check if borrow from most significant bit

OF: Overflow flag. When the signed result of a math operation is too big to be stored within the word size.

PF: Parity flag. Checks for corrupt data as a result of a math operation. Now its antiquated and only works with 8bit values

AF: Adjust/Auxilliary flag. Binary coded decimal math operations. Check if borrow from bit 3 of register

ZF: Zero flag. Check if result of math operation is zero

SF: Sign flag. Sign if the result is negative or positive. This is the exact same as the leftmost bit of the register

  

Control flags:

Used to control specific process behaviors.

DF: Direction flag. Controls the ways strings are handled by the processor. Can be used to change how strings are read like from top address or bottom address.

  

System flags:

Used to control OS level operations which should NEVER be modified by any program or application

TF: Trap flag. Enables single step mode. Instead of manual step intos, the program auto steps

IF: Interrupt enable flag. Controls how processor responds to external interrupts

IOPL: I/O privilege level flag. Indicates I/O privilege level of current tasks. Tasks using I/O devices cannot exceed this level, else they will not trigger.

NT: Nested task flag. Controls whether current task is linked to previous task and used for chain interruptions of tasks

RF: Resume flag. Controls how the processor responds to exceptions when in debug mode

VM: Virtual-8086 mode flag. Indicates the processor is running on a virtual machine

AC: Alignment check flag. Used in tandem with AM bit in CR0 to enable alignment checking of memory references

VIF: Virtual interrupt flag. Replaces the IF flag if in virtual machine

VIP: Virtual interrupt pending flag. Indicates that an virtual interrupt is pending

ID: Identification flag. Indicates whether the processor supports CPUID instructions

  