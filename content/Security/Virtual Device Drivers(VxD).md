---
tags:
  - os
---
The x in VxD stands for anything. It is a virtual _ driver. Virtual network driver, virtual software driver, virtual kernel drivers, etc.

Early in the DOS days, the computers would only be able to run one program at a time, as at that moment they were not built for multitasking. A process would have total 100% control over the hardware. Later, they split each process into its own virtual machine. In order to allow these virtual machines to communicate with eachother, they introduced VxDs. Every device interrupt on this machine would be sent to a virtual device first which the OS could handle, preventing clashes with interrupts from different processes.

As of now, they are just a neat bit of history from the early dos periods