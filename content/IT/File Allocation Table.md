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
# Areas
![[File Allocation Table-20260314000942844.webp]]
- System area: stores volume boot record and FAT tables
- Data area: stores root directory and files
# File Allocation Table
Keeps trace of which clusters files are stored at.
Every cluster is given an [[Logical Block Addressing|LBA]] address, and a cluster status.
![[FAT32-20240704014144107.webp|306]]
### Statuses
- **0x0:** Open for storing data
- **0x0000FFF7:** Bad block. All drives - even the newest ones will have minor imperfections that result in certain blocks being unusable. The OS locates these bad blocks and marks them as the unusable status to prevent data being stored in them.
- **0x0000FFFF:** End of file marker
- **0x\*\*\*\*\*\*\*\*:**  A pointer to another address that stores the start of the file.
  ![[FAT32-20240704020734789.webp|352]]
# FAT Types
- [[FAT16]]
- [[FAT32]]
- [[exFAT]]
# Concepts
- [[Volume Boot Record]]