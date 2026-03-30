---
tags:
  - file_system
---
Keeps trace of which clusters files are stored at.
Every cluster is given an [[Logical Block Addressing|LBA]] address, and a cluster status.
![[FAT32-20240704014144107.webp|306]]
### Statuses
- **0x0:** Open for storing data
- **0x0000FFF7:** Bad block. All drives - even the newest ones will have minor imperfections that result in certain blocks being unusable. The OS locates these bad blocks and marks them as the unusable status to prevent data being stored in them.
- **0x0000FFFF:** End of file marker
- **0x\*\*\*\*\*\*\*\*:**  A pointer to another address that stores the start of the file.
  ![[FAT32-20240704020734789.webp|352]]