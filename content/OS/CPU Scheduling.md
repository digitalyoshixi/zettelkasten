---
tags:
  - os
  - scheduling
---
The basis of multiprogrammed OS. because of CPU scheduling, your OS can switch among processes seamlessly. Several processes are kept in the memory at one time. When one process has to wait, the OS gives CPU to another process.

  

### CPU and I/O Burst

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv93_tmp_8a11b19ad165f93b.png)  

A process execution can be in the states of CPU execution or I/O wait. Every process execution alternates between these states. CPU burst, I/O burst, CPU burst, I/O burst,…until the process is complete. Eventually the final CPU burst ends with a termination request.

### Preemptive & Non-preemptive scheduling

CPU scheduler: Whenever the CPU becomes idle due to an I/O burst, the CPU scheduler will select a process in the memory to execute.

Dispatcher: the module that gives control of the CPU to the process determined by the CPU scheduler. There is often latency when switching CPU, this latency is regarded as dispatch latency.

We decide when to schedule a switch in the following scenarios:

1. When process switches from running -> waiting (I/O Burst)
    
2. When process switches from running -> ready(Interrupt)
    
3. When process switches from waiting -> ready(finished I/O Burst)
    
4. When process terminates
    

For situations 1 and 4, a switch happens 100% of the time. For situations 2 and 3, switches only occur if the ready process has higher priority.

When scheduling occurs due to case 1 or 4, the scheduling scheme is non-preemptive. For cases 2 and 3, we call it preemptive. For preemptive scheduling, the current running task may be taken away before it terminates.