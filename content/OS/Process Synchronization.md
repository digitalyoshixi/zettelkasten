---
tags:
  - os
  - synchronization
---
Cooperating processes affect other processes by sharing data, but if multiple processes try sharing data concurrently, then it will lead to data inconsistency. The race condition is the condition that data is modified. Chronologically speaking, if 2 processes modify at the same time, then data will have to only accept one of these outcomes and not both.

[[Critical Section Problem]]
  