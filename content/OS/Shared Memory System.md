---
tags:
  - os
---
This sort of communication requires a region of shared memory. The shared memory region resides within the process that created it.

Eg. process A makes the memory region, process B will take data from address space from process A. Process A will take data from address space in process A as well.

**Normally the OS prevents processes from accessing another processes’ memory. To share memory, the 2 processes agree to remove this restriction.**

You will see these memory systems in cases like compiler & assembler, interweb & user. A producer and producer while a consumer consumes in synchronicity.

As for buffers(temporary storage for moving data), you can have 3 types

- Zero capacity: can't add more data until message recieved
    

- Unbounded buffer: No limit to amount of data stored
    
- Bounded buffer: limited data storage