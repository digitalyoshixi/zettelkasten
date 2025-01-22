---
tags:
  - windows
  - partitioning
---
A [[Partitioning]] scheme used in modern windows systems.
Partitions are referred to as volumes, with the main differences from [[Master Boot Record|MBR]] being:
1. You can have as many volumes as you want
2. You can use software to modify and create partitions
# Volume Types
![[Windows Dynamic Disks-20240703211343556.webp]]
- **Simple Volumes:** Very similar to primary partitions in [[Master Boot Record|MBR]]. They show up as letters like: `C:/`, `D:/`
- **Spanned Volumes:** A single Drive that is the unallocated space on all drives.
- **Striped:** [[Disk Striping|RAID 0]] volumes
- **Mirrored:** [[Disk Mirroring|RAID 1]] volumes
- [[Redundant Array of Independent Disks|RAID 5]] volumes
