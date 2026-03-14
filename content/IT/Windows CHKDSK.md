---
tags:
  - windows
  - partitioning
---
A windows tool to check disks for hardware issues and flag them appropriately.
1. It check for [[File Allocation Table Filesystem|bad blocks]] on a [[Hard Drive|HDD]]. When it finds a bad block, it will flag it appropriately (0x0000FFFF for FAT file systems).
2. It looks for filenames no longer linked with clusters and removes them (Fixes logical file system errors)
# Flags
### /f
Fix all errors on disk
### /r
Locate bad sectors and recover readable information
