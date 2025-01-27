---
tags:
  - reverse_engineering
  - memory
---
### Part 16: Heap:

The heap grows upwards!!! FINALLY ANOTHER ERECT SYSTEM!!! The heap is the region of memory that needs to be managed manually. It's a free floating region of memory that is larget than the stack’s allocation.

Built in C functions like malloc() or calloc() will allocate memory. free() will deallocate memory. If you dont free the memory, then your program suffer a memory leak. This means there will be no free space for other processes that need memory. Unlike the stack, the heap does not have size restrictions, only thing that affects it is your PC limitations. Heap is slower to read and write to, and you have to use pointers to access memory.

Unlike stack, variables in the heap are accessible by any function meaning these are global variables. If you need large variables like arrays or structures, use the heap as it can also dynamically allocate memory.