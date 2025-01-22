---
tags:
  - os
---
Interrupts to cause the OS to change their current task to a different task. When these interrupts occur, the system saves its progress known as context. The context is saved in the process control block(PCB) similar to a bookmark; this is a state save. When we want to restore these contexts, we would perform a state restore. The process of switching from state save to state restore is known as the context switch.

A context switch involves one process being state saved, and another being state restored.

The context switch is overhead. This means no useful work is being done when a context switch is performed. But these times are usually less than a millisecond