---
tags:
  - memory
  - os
aliases:
  - RVA
---
A virtual address signifying the distance from the base address of a file.
Used for mapping physical memory and software by creating a page table used between the two.
# Advantages
1. Multiple address spaces. Each address space is its own isolated table which only is seen by the program which needs it. It ensures programs are completely isolated from one another. A crash in one process will not poison another.
2. Memory is given rules. Which is writable, which is readable, which is executable To allow this though, means each section must start on a different page. Since default section page size is 4kb(4096 bytes), this makes some programs a lot bigger size then they actually are. So there is another page size. 512 bytes, which is for files
3. Harddisk temp storage. It allows some apps, if they are idle and unused currently, to store its pages into the hard disk to allow more space in the RAM. If the app needs to be run again, we just reverse the situation and bring those pages from the hard disk back to the RAM