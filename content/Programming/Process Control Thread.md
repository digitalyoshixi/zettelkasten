---
tags:
  - os
  - programming
aliases:
  - Thread
  - Process Thread
---
A single separated control flow of a program. Each thread has:
- Seperate thread ID
- Separate [[Program Counter Register|PC]]
- Separate [[Register|Registers]]
- A subsection of the [[OS Stack|Stack]] (increments stack pointer)
- Shares original [[Process]] [[Data Section]]
- Shares original [[Heap]]
A traditional process has a single thread. If you have more than one thread, you can perform multiple tasks at the same time.
Fast to create and switch between.
# Ideas
 - [[Multithreading]]
 - [[Hyperthreading]]