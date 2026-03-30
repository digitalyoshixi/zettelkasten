---
tags:
  - hardware
aliases:
  - CPU
---
![[CPU-20240516004654998.webp|315]]
The main processing unit used to calculate all the essential computer operations.
- Arithmetic
- Controlling
- Logic
- I/O operations
Every piece of hardware, including the motherboard depend on the CPU architecture
# How it works
### [[External Data Bus]] 
Used to transmit CPU data to peripheral devices
### [[Register]]
Used to perform logic operations. Depending on the CPU architecture the register can be 8 - 64bit. 32bit has eax, 64bit has rax. The most basic CPU has 4 registers ax, bx, cx, dx
### [[x86 Assembly|Assembly]]
Other devices use [[External Data Bus|EDB]] to sen machine codes which are assembly language to instruct the CPU what to do to the registers. This is again, binary data, but they are given mnemonics like `mov eax, ebx` which moves the value of `ebx` into `eax` in x86 assembly.
### [[Clock Signal|Clock Wire]]
The CPU only reads from the [[External Data Bus|EDB]] when given a clock signal. For certain operations, this means that between 2 - 1000 clock signals must be sent.
![[Central Processing Unit-20240516012829222.webp]]
Frequency of recieving these clock signals is determined by the CPU. 
For example, the AMD threadripper has a base clock speed of 2.5 GHz. which means it takes $2.5*10^9$ clock signals / second
##### [[Crystal Oscillator]]
A piece of quartz made to act as an oscillator that sends out electric pulses at a constant speed millions of times per second. It acts as the metronome required by the clock wire to have constant frequency.
It is usually built into the motherboard as you don't need to replace it often.
### [[Memory Chip Controller]]
This chip allows the CPU to retrieve memory from a specific memory address.
### [[Arithmetic Logic Unit]]
The part of the CPU that computes arithmetic
# Advanced CPU Features
- [[CPU Clock Multipliers]]
- [[64-Bit Processing]]
- [[Virtualization]]
- [[CPU Parallel Execution]]
- [[Multicore Processing]]
- [[Graphics Processing Unit]] (Integrated)
- [[Data Execution Prevention]]
# Other CPU Concepts
- [[Mobile CPUs]]
- [[CPU Labelling]]
- [[CPU Bus Terminology]]
- [[CPU Socket]]
- [[CPU Compatibility List]]
- [[CPU Installation]]
- [[Overclocking]]
- [[CPU Overheating]]
- [[CPU Architecture]]
- [[CPU Cache]]
- [[CPU Thread]]