---
tags:
  - os
  - scheduling
---
A priority is associated with each process and the OS assigns the CPU to the process with highest priority.

Priority scheduling can either be preemptive or non-preemptive. It depends if a newer process has higher priority than the one currently in the CPU.

  

Priority scheduling in its nature only allows higher priority processes to run first. Problems arise when you need lower priority processes to execute. If you are on a heavily loaded system then processes enter steadily, never allowing lower priority processes to run.

We solve this problem by giving all processes aging techniques. The longer a process stays in waiting, the more priority the accumulates.

