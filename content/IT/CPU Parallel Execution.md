---
tags:
  - computer_organization
  - cpu
---
The ability for a CPU to process several assembly commands at the same time. 
# Pipelines
![[Central Processing Unit-20240519215101310.webp]]
Assembly commands are broken up into tasks. There are specific circuits responsible for a each task
This way, circuits can work when the other circuits are working too, rather then relying on the entire operation to finish. 
### [[Pipeline Stall]]
Certain commands take more than once clock cycle to complete. When this happens, the pipeline is stalled and must wait for the bottleneck to finish.
### Pipeline Optimization
- [[Operand Forwarding]]
# Cache/SRAM
Pipe lining will always occur in CPU, leading to desynchronization between RAM and CPU, where the RAM must wait to send the next instruction.
![[CPU Parallel Execution-20240520155340846.webp]]
This leads to later delay when the CPU finishes its operation, it must wait for the RAM to send over the operation
![[CPU Parallel Execution-20240520155452768.webp]]
We never want to CPU to be idle, so to reduce wait states, SRAM is introduced.
![[CPU Parallel Execution-20240520160423706.webp]]
Many modern CPUs use multiple caches L1, L2, L3. 
Each core contains their own L1 and L2 caches, the entire CPU shares the L3 cache.
Intel calls this [[Smart Cache]]
# Multithreading
Ability to run multiple threads at the same time, effectively creating multiple CPUs.