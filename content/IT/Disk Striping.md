---
tags:
  - IT
aliases:
  - RAID 0
---
Splitting data across multiple drives.
Certain chunks of data is stored in drive 1, another portion into drive 2, another in drive 3, etc.
This makes accessing data much faster.
The downside is that there is no redundancy of [[Disk Mirroring]]/[[Disk Duplexing]] and if one drive fails, all data is lost.
# Disk Stripping with Parity
![[Disk Stripping-20240702232658541.webp]]
Parity gives the function of protecting data in disk stripping setups and can recover data if one of the drives fails.
It requires atleast 3 drives and uses that extra drive as the space for backup (so essentially, one drive is lost)
# RAID 0 Failure
When a drive in a RAID 0 array fails, you must replace the bad drive then restore from a backup.