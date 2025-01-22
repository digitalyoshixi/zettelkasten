---
tags:
  - os
  - synchronization
---
Software solution to the critical section problem. Uses a single integer value called semaphore and 2 atomic operations wait() and signal()

S - Semaphore. Default value is 1

P - Wait. if S > 0, then we wait. After the wait, we decrement the value of S so it is now 0

V - Signal. Opening S for other processes. S is now 1

Weirdly though, semaphore modification is indivisible so it faces a similar miniature critical section problem of only allowing S to be modified by one process at a time. S is shared between all processes

Semaphores can be binary/mutex locks or a counting semaphore for different instances

  

The semaphore suffers from busy waiting. We are stuck in a spinlock as all processes must ‘spin’ due to a lock(check for semaphore value). What a process can do is block itself. Instead of being in a while loop and spinning, we put it in the waiting queue

You may also encounter deadlocks(bruh) when 2 processes wait for 2 different semaphores