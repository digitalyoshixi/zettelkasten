---
tags:
  - os
  - scheduling
---
Classes of scheduling algorithms are created in which processes are divided into 2 groups based on their response time requirements and scheduling needs:

1. Foreground queues(interactive)
    
2. Background queues(Batch)
    

Foreground processes usually have priority over background processes. Fixed-priority preemptive scheduling dictates the behavior of foreground queue priorities over background queues.

  

Foreground and background queues are permanently assigned to one queue based on their properties in memory size, priority. Each of these queues have their own DIFFERENT scheduling algorithm like FCFS,RR, etc.

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv9f_tmp_1e5f4b0cd87e1233.png)

  

### Multilevel feedback-queue scheduling

This allows processes to move between queues. An example is a process that has high CPU burst will be moved lower, and a process that has aged will move higher.

A multilevel queue scheduler is defined by:

- \# of queues
    
- Scheduling algorithm for each queue
    
- Method to determine priority
    
- Method to determine which queue a process needs to enter when the process needs a service