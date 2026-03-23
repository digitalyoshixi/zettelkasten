---
tags:
  - os
  - file_system
aliases:
  - MFT
  - $MFT
---
An enhanced FAT table that exists in first chunks of the disc.
- Tracks changes of all objects (files, folders)
- Each object has its own record in the MFT file
- MFT stored at root of NTFS partition
A backup of the MFT exists in the middle of the disk.