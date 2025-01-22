---
tags:
  - memory
  - hardware
aliases:
  - MCC
  - IMC
---
![[Memory Chip Controller-20240516220507337.webp|464]]
MCC allows communication between CPU and RAM. It ensures that the CPU can retrieve memory from a specific address.  The MCC lays on the motherboard.
Modern day MCC can retrieve and send 64bits from its address bus consistently
### Communication
The MCC is connected to the CPU with several Address buses. The address bus collection signifies the address of memory requested through a series of whether the current is on or off for each bus.
This means the more address buses you have, more bits can be transferred at each cycle.
![[Memory Chip Controller-20240516220840204.webp|428]]
# Integrated Memory Controller
To make things faster,  the CPU has its own version of the MCC integrated inside of the chip. It may still use the motherboard one, but IMC will be prefered. 