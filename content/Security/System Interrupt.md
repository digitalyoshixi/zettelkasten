---
tags:
  - os
aliases:
  - Interrupt
  - Hardware Interrupt
---
Asynchonous communication that the [[Operating System|OS]] sends to the [[Central Processing Unit|CPU]] whenever an [[Input Output|IO]] device updates.

Used for:
- Keyboard inputs
- Network data
- Hardware faults
When the CPU receives an interrupt, it stops what its doing and jumps to an [[Interrupt Handler]] routine.

In contrast to [[System Polling]]