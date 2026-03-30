---
tags:
  - os
aliases:
  - I/O Controls
  - IOCTL
---
Commands for direct communication between [[Protection Ring|Userland]] and [[Protection Ring|Kernel Space]].
IOCTLs allow application to communicate with kernel mode device driver.
# Attacks
- Hooking IOCTL functions to filter results or modify control flow