---
tags:
  - os
  - programming
aliases:
  - Thread
---
A single control flow of a program. Each thread has:
- A thread ID
- A [[Program Counter Register|PC]]
- [[Register|Registers]]
- A subsection of the [[OS Stack|Stack]] (increments stack pointer)
- Shares original [[Process]] [[Data Section]]
- Shares original [[Heap]]
A traditional process has a single thread. If you have more than one thread, you can perform multiple tasks at the same time.
# Ideas
 - [[Multithreading]]
 - [[Hyperthreading]]