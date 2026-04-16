---
tags:
  - os
  - synchronization
---
Software solution to the [[Critical Section Problem]]. 
Uses a single integer value called semaphore and 2 atomic operations:
- wait()
- signal()
# States
- S - Semaphore. Default value is 1
- P - Wait. if S > 0, then we wait. After the wait, we decrement the value of S so it is now 0
- V - Signal. Opening S for other processes. S is now 1