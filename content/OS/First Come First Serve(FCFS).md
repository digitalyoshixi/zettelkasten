---
tags:
  - os
  - scheduling
---

The process that requests the CPU first will get the CPU first. Also take in account first in, first out. The process will also be the first to leave. All other processes must wait for the first process to finish so that they can have their turn.

Average waiting time is quite long if there are long processes in the line

The FCFS algorithm is non-preemptive because processes are not interrupted

  

### Convoy effect

If processes with higher burst time arrive, then smaller burst processes must wait a long time for the processes to complete.

  

Turnaround time = completion time - arrival time

Turnaround is NOT the same as burst time because burst time is time that process takes to complete unvaried, turnaround time includes the time of waiting for I/O operations.

Waiting time = turnaround time - burst time

  

Overhead is the same as delay. Some processes may face an overhead before they can be assigned to the CPU.

When we have overheads, we must then find efficiency using the method useful time/total time