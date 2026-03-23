---
tags:
  - memory
  - os
aliases:
  - Paging
  - Swap
---
Page file is the file that contains all processes to be swapped in [[Virtual Memory]].
This is similar to swap partitions in linux
# `pagefile.sys`
Windows will automatically create a pagefile located at:
```
C:\pagefile.sys
```
If deleted, windows will make a new one
# Process
![[Virtual Memory-20240524053746233.webp|665]]
1. A new process wants to load, but there is not enough free RAM for it
2. A offscreen process(es) are unloaded from RAM and copied into a [[Page File]] saved to the hard drive
3. When you need the offscreen process(es) they are loaded into memory quickly, then unloaded, then reloaded. This is the swap