---
tags:
  - file_system
aliases:
  - FAT
---
![[FAT32-20240704021052826.webp|439]]
File system most commonly used on drives with less than 32GB (like [[USB Flash Drive]]).
The cluster size varies, but for our example lets say clusters are one [[Hard Drive|Block]] (4096 bytes or 4-KB). 
Most files are larger than 4096 bytes, so they must be stored in several clusters.
If a file is smaller than 4096 bytes, then we have wasted space (which we have to just accept because most of the time this wont happen)
# FAT Types
- [[FAT12]]
- [[FAT16]]
- [[FAT32]]
- [[exFAT]]
# Areas
![[File Allocation Table-20260314000942844.webp]]
- System area: stores volume boot record and FAT tables
- Data area: stores root directory and files
# Concepts
- [[Volume Boot Record|Boot Record]]
- [[File Allocation Table]]
- [[FAT Data Area]]
- [[FAT Data Recovery]]
- [[FIle Slack]]