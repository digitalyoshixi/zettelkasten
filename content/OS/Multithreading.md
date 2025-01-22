---
tags:
  - os
aliases:
  - Hyper-Threading Technology
  - HTT
---
We have user threads and kernel threads. We must establish a relationship between user and kernel threads. There are 3 ways to do this:

1. Many to one model:one kernel thread and several user threads.
    
- Thread management is done by a thread library so its easy
- Entire process will block if a thread makes a blocking call
- No multithreading
    

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv8x_tmp_95563fec711f99ca.png)

2. One to one model: pairs of user threads to kernel threads.
    

- Multithreading
    

- Must have both user and kernel thread at once. Slower performance the more threads you have
    

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv8x_tmp_c17299df30212b8f.png)

3. Many to many: all user threads and all kernel threads connect to one central location
    

- Almost the same # of kernel threads to # of user threads
- Multithreading
- Blocking won't disrupt system
    

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2iv8x_tmp_27700cadd82e5bb2.png) 
### Hyperthreading/Simultaneous Multithreading(SMT)
Same as Multithreading but used by Intel. CPU cores matter for multithreading.
![[Multithreading-20240731003448743.webp|513]]
A single core can have multiple threads