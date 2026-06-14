---
tags:
  - os
aliases:
  - Linux Program Memory Layout
  - Program Address Space
  - Virtual Address Space
  - Linux Process Memory
---
The space that a [[Linux Process]] gets during [[Linux Process Loading]].
A collection of [[Memory Page]]
![[Program Memory Layout-20250829224210554.webp|427]]
- Size is from 0-$2^{32}-1$
# Sections
- Libraries
- [[OS Stack]]
- [[OS Heap]]
- Memory mapped by the program
- Helper regions
- Kernel code in upper half of memory inaccessible to process
- The binary
	- `.text`
	- `.data`
# Page States
# Viewing Virtual Memory space
You can see the program's memory space at `/proc/self/maps`