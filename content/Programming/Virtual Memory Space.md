---
tags:
  - os
aliases:
  - RAM Layout
  - Program Memory Layout
  - Program Address Space
  - Virtual Address Space
---
The space that a [[Linux Process]] gets during [[Linux Process Loading]].
![[Program Memory Layout-20250829224210554.webp|427]]
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
# Viewing Virtual Memory space
You can see the program's memory space at `/proc/self/maps`