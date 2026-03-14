---
tags:
  - os
  - file_system
aliases:
  - VBR
  - Boot Record
---
Part of the system section of a [[File Allocation Table Filesystem|FAT]] table.
Contains information about the volume and boot code to continue to the boot process for the [[Operating System|OS]].
# Primary Partition
Has sectors 0,1,2 and backup in sectors 6,7,8
![[Volume Boot Record-20260314002523179.webp]]
Contains:
- Jump instruction for system to continue booting (offset `0x00`)
- [[Original Equipment Manufacturer|OEM]] ID to show which OS was used to format device (`0x03`)
- 