---
tags:
  - os
---
Systems divided by number of general purpose processors.

### Single processor systems - Only 1 cpu

Execute general purpose instructions. Microprocessors must also be present. Eg. small microprocessor in keyboard to convert keystrokes to binary data. Even though microprocessors count as more than 1 processor, Single processor system is still considered single because there is only 1 general processor.  

### Multiprocessor/Parallel/Tightly Coupled systems - multiple cpus

2 or more processors in close communication. Often sharing the clock, memory and bus. Allows for better performance, reliability and compatibility.


Symmetric processing: All CPUs are similar and work on the same task

Asymmetric processing: Master CPU which monitors other CPUs(slaves) who work on different tasks.


### Clustered systems - multiple systems

2 or more systems together. Requires multiple CPUs to accomplish work. If one system fails, the entire system can still keep running


Symmetric structure: All hosts run different applications and monitor each other

Asymmetric structure: One machine in Hot-Standby mode to monitor. If one other system fails, it takes its place. All other systems are running applications