---
tags:
  - os
---
A program designed to locate the operating system drive.
The process of finding it is different across [[Motherboard Firmware]]
### BIOS
Reads the [[Complimentary Metal-Oxide Semiconductor Battery|CMOS Battery]] data to find this location. From the boot priority list, it picks the first drive that has a valid [[Partitioning|Boot Sector]].
### UEFI
[[Power-On Self-Test|POST Program]] hands control of boot process to [[Boot Manager]]. Boot Manager loads operating system directly