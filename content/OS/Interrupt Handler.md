---
tags:
  - hardware
  - os
---
A piece of [[Assembly]] code called whenever the [[Processor]] recieves an [[System Interrupt]].
# Process
1. Determine the cause using special registers
2. Handle what the interrupt requires
	1. Read/Write from device
	2. Deal with memory issues
	3. Terminate program
3. Return to original code
# Types of Handlers
- [[Polled Handling]]
- [[Vectored Handling]]
- [[Interrupt Descriptor Table]]