---
tags:
  - IT
aliases:
  - GPT Partitioning
---
The partitioning scheme for modern [[Unified Extensible Firmware Interface|UEFI]] [[Mass Storage Device|Drives]] or drives over 2TB.
It improves on [[Master Boot Record|MBR]] by allowing for:
- Up to 128 partitions
- Support for drives larger than 2.2 TB
# LBA Arrangement
![[GUID Partition Table-20240703214101596.webp|348]]
Partitions are sectored based off [[Logical Block Addressing|LBA]]. 
### Protective MBR (LBA 0)
Protective MBR is serves to have backwards compatability with MBR. It is also commonly used to prevent MBR disk utility software from overwriting GPT disks accidentally.
### GPT Header (LBA 1)
![[GUID Partition Table-20260313225952027.webp]]
Includes a [[Pointer]] to the Partition Entry Array.
A GPT Header backup exists in the final LBA aswell.
### Partition Entry Array (LBA 2)
The list of partition entries on the drive.
The entries usually follow this format:
![[GUID Partition Table-20240703215545225.webp]]
They are defined by a set partition size (commonly 128 bytes)