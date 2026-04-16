---
tags:
  - os
---
Saving the state of a [[Process Control Block|PCB]] during [[System Interrupt|Interrupt]].
When the process can continue, it restores the [[Process Control Block|PCB]] state.

The context switch is overhead. This means no useful work is being done when a context switch is performed. But these times are usually less than a millisecond