---
tags:
  - memory
  - hardware
  - synchronization
aliases:
  - RAID
  - Redundant Array of Inexpensive Disks
---
![[Redundant Array of Independent Disks-20240525231840180.webp|213]]![[Redundant Array of Independent Disks-20240525232122103.webp|248]]
A [[Mass Storage Device]] utilizing multiple storage devices to be used as:
1. A contiguous block of memory
2. Independent disks that can back eachother up 
# RAID Forms
- [[Small Computer System Interface|SCSI]]
# RAID Levels
![[Redundant Array of Independent Disks-20240702234042147.webp]]
- [[Disk Striping|RAID 0]]
- [[Disk Mirroring|RAID 1]]
- [[RAID 5]]
- [[RAID 6]]
- [[Disk Nested Strips|RAID 10]]
- [[Disk Nested Mirrored Strips|RAID 01]]
# RAID Implementation
### Software Monitors
Literally free, given that you have [[ATA S.M.A.R.T]] software.
Windows has a built in RAID software called "Disk Management"
### Hardware Monitors
You can purchase a SATA RAID controller
![[Redundant Array of Independent Disks-20240702234451860.webp]]
These controllers have their own CPU and memory that can handle the work of maintaining and implementing RAID.
Hardware based RAID is invisible to the OS, so configuring it will usually occur before the OS boots.
![[Redundant Array of Independent Disks-20240702234627367.webp]]
# RAID Concepts
- [[Disk Mirroring]]
- [[Disk Duplexing]]
- [[Disk Striping]]
- [[Disk Nested Strips]]
- [[RAID Boxes]]
- [[RAID Troubleshooting]]
- [[RAID Resync]]
