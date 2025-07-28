---
tags:
  - os
  - partitioning
aliases:
  - Boot Sector
  - Root Sector
  - Volume
---
The process of subdividing a physical drive into partitions which are blocks of memory designated for specific purposes.
After partitioning, you will need to [[Disk Formatting|Format]] the disk.
# Concepts
- [[HDD Sectors]]
- [[SSD Blocks]]
- [[Logical Block Addressing]]
- [[Mount Point]]
- [[Storage Pools]]
# Partitioning
Assigning [[Logical Block Addressing|LBA]] ranges a purpose.
![[Partitioning-20240703010125423.webp|365]]
you can partition a hard drive to store multiple [[IT/Operating System|OS]]
# Partitioning Schemes
- [[Master Boot Record|MBR]]
- [[Windows Dynamic Disks]]
- [[GUID Partition Table|GPT]]
# Partitoning Tools
- [[FDISK]]
- [[Windows Disk Management]]
- [[diskpart]]
- [[GParted]]