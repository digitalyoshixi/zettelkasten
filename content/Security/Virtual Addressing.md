---
tags:
  - os
  - memory
aliases:
  - Virtual Address
---
Most OSes use virtual memory. Mapping of virtual address space to a physical address space. This is useful because, with a virtual address space, you can have a contingious block of memory. Its a lot easier to find offsets in a disk file in the memory because of virtual address spaces.

Virtual addressing is critical for datatypes like arrays, because arrays heavily require offset addresses to even parse through them.

A few more boons are as follows:

- Memory isolation(for security)
    
- More memory than physically able(paging)
    
- Applications do not have to manage shared memory space

This technique is commonly paired with [[Relative Virtual Addressing]]

### Example Mapping

![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivev_tmp_c116727bfd3f71ab.png)

It is essentially a 1-1 mapping, but addressess will not be linearly mapped and not the same size exactly.