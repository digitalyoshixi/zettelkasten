---
tags:
  - os
  - scheduling
---
The algorithm reads each process’s CPU burst. It assigns the CPU to the task that has the smallest burst time. If 2 processes have the same burst time, then we follow FCFS. SJF is faster than the FCFS algorithm.

The SJF algorithm can be preemptive or non-preemptive. It depends on the arrival time of a new process. The quicker process will always overtake the longer one, even if the longer one is in execution.

  

Waiting time = total waiting time - milliseconds process executed - arrival time

  

The problem with SJF scheduling is that there is no way to know the length of the next CPU burst, we need to predict its value.