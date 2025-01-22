---
tags:
  - os
---

A computer system consists mainly of a CPU and a number of shared devices connected to a common bus so they can share memory. Whenever something is executed, it has to be loaded into the main memory(RAM).

All devices can execute concurrently. This is possible because of the memory controller

### [[Bootstrap Loader]]
Code executed before the operating system begins to run. They send instructions on how to boot. It loads the OS kernel into the main memory and then the OS starts.

### [[System Interrupt]]
Tells you to stop doing this work to do something else. A Hardware or Software input will tell the CPU to execute this action instead. Usually sent through help of the system bus

### [[Syscall]]
Software interrupts are called System calls or Monitor calls

When CPUs are interrupted, it stops what it is doing, enters a fixed location in the memory. The location is the starting memory address of where the interrupt was located. Once finished executing, it returns to the task it was doing beforehand.