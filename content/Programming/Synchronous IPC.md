---
tags:
  - programming
  - os
---
A method for Asynchronous [[Message Passing]].
- Forces multithreaded code, poor choice for multi-core
![[Synchronous IPC-20260816232436620.webp]]
# Process
1. Sender program blocks until next program is ready to recieve
2. Kernel copies data from sender's memory space to reciever's memory space (from sender's context, triggers [[Context Switch]])