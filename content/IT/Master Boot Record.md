---
tags:
  - partitioning
aliases:
  - DOS Partitioning
  - DOS
  - MBR
---
A [[Partitioning]] scheme frequently used in PC DOS computers.
![[Master Boot Record-20240703014236462.webp]]
# Master Boot Record Code
Drives that use the MBR partitioning scheme will have a master boot record in their first sector. The master boot record includes information about the installed operating systems and how to boot it.
# Partition Table
A table that includes the # of partitions and size of partitions on the disk.
The MBR partition table supports only 4 partitions max.
After the MBR code finds the partition with the OS, the partition boot sector loads that OS.
# Partition Types
### Primary Partitions
Partitions for bootable operating systems.
These show up in windows like:
`C:/`
`D:/`
...
`Z:/`
The MBR code knows which OS is the main one, as the main partition will have a active flag to signify its the main OS.
[[Grand Unified Bootloader|GRUB]] allows us to configure this active flag to change the OS to boot into
### Extended Partitions
Partitions that should not be bootable.
These can contain logical drives which are also assigned letters.
![[Master Boot Record-20240703015051767.webp|361]]
### Hidden Partition
A primary partition that is hidden from your OS.
Most commonly used for backups
### [[Virtual Memory|Swap]] Partition
Partitions on your drive, designated to be used as RAM when your system needs more RAM.