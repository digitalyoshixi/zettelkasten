---
tags:
  - hardware
aliases:
  - SCSI
---
![[Small Computer System Interface-20240717210503318.webp]]
A [[Redundant Array of Independent Disks|RAID]] technology designed to string many peripherals together onto a single controller.
It uses a SCSI bus to connect other [[Mass Storage Device]] like HDD, SDD, Floppy drives, etc.
It comes in [[Parallel AT Attachment|PATA]] and [[Serial AT Attachment|SATA]] forms, but both have the same command set, so the 2 technologies can be used in same computer.
# SCSI Interfaces
![[Small Computer System Interface-20240730192403373.webp]]
# Daisy Chaining
![[Small Computer System Interface-20240730193037202.webp]]
- Connecting each device with [[Parallel AT Attachment|PATA]]
- Allows for 16 devices in a chain
### SCSI ID
ID for each **physical** device.
Is not able to see smaller storage drives
### Logical Units (LUNs)
- Allows viewing of smaller storage drives within a larger SCSI device like storage arrays or virtual machines
- Allows for identifying [[Partitioning|Partitions]]
### Terminators
A device to tell when the chain ends.
Required to allow for several communications simultaneously
# SAS (Serial Attached SCSI) Forms
![[Small Computer System Interface-20240730193506438.webp|534]]
An enhancement to SCSI technology that uses point-to-point connections rather than daisy chains.
**SAS-4:** Provides speeds up to 22.5 Gbps
