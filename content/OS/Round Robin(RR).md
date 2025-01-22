---
tags:
  - os
  - scheduling
---

Designed for time sharing systems. It is like FCFS but it is preemptive so processes may be switched at any time. A small unit of time in this algorithm is called a time quantum/slice and generally lasts from 10-100 milliseconds.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv9d_tmp_d38c3fb42643cac1.png)  

The ready queue is a circular queue. It goes around the queue and allocates the CPU to all of them it passess through for one time quantum. The queue is created in the format of FCFS.

  

Processes that are completed within 1 time quantum are completed, those that are not are sent to the end of the line with saved context.

  

Turnaround time = completion time - arrival time

Waiting time = turnaround time - burst time

OR

Waiting time = last start time - arrival time - (Preemption * time quantum)