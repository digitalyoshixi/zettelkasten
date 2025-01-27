---
tags:
  - reverse_engineering
  - assembly
  - x86
---

### Part 9: x86 basic architecture

A computer application is a table of machine instructions to be stored in memory, then converted into binary so the processor can deal with them. CPU, Memory and I/O devices are all connected via system bus.

The CPU consists of 4 different parts which are:

1. Control unit. Storing, retrieving, decoding from CPU to memory
    
2. Execution unit. Where execution and fetching instructions occurs
    
3. Registers. Temporary data storage during execution
    
4. Flags. Indicate special events during execution
    

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivae_tmp_34b08e356d50e690.png)

Cpus tend to run like such:

1. Cpu fetches 4 bytes from the memory
    
2. Cpu loads it
    
3. Cpu reads binary pattern
    
4. Cpu executes its procedure
    
5. Memory pointer changes to next address and process repeats
