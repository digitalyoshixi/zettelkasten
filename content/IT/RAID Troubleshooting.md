---
tags:
  - hardware
---
# Drive Not Recognized
The RAID implementation (whether it is software or hardware) does not recognize a drive. May be due to:
- firmware issues
- disconnected drives (certain motherboards require specific RAID connectors)
# RAID Failure
A drive dies in a [[Disk Striping|RAID 0]] array. You should use [[ATA S.M.A.R.T|ATA SMART]] reader software to diagnose the cause.
# RAID Not Found
Mostly due to the model of RAID or implementation of RAID.
software implementations of RAID are often inconsistent and proper hardware implementations should always detect drives.
# Orange Light
- Hardware problem with the hard drive