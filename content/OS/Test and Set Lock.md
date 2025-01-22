---
tags:
  - os
  - synchronization
---


Hardware solution to the critical section problem. We have a boolean lock. Every process checks If the lock is true, if it is then it cannot enter and must wait for it to be unlocked. When the program exits the critical section, it sets lock to false.

The bad thing about this solution is that there is no bounded waiting. New processes could replace older processes in the waiting queue.