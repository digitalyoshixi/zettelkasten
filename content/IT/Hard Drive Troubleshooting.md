---
tags:
  - memory
---
# Partitioning Errors
**Failed to partition at all:** The drive doesn't show up in [[Windows File Explorer]], it only shows up in [[Windows Disk Management]]

If you have the wrong size or wrong type of partition, you can use the [[Windows Disk Management]] to fix that.
# Formatting Errors
Failure to format leads to a "is not accessible" prompt by [[Windows File Explorer]]. 
# Lost Allocation Unit
For the most part, hard drives are dying and will have blocks that are inaccessible. If you frequently, get lost allocation units, then the drive is almost dead and needs to be replaced.
This can be diagnosed with [[ATA S.M.A.R.T|ATA SMART]] tools.
![[Hard Drive Troubleshooting-20240704044845937.webp]]
# Data Corruption
Data gets corrupted by:
- Power surges
- accidental shutdowns
- corrupted installation media
- [[Malware]]
Errors messages that hint to file corruption can be:
- "The following file is missing or corrupt"
- "The download location information is damaged"
- "Unable to load file"
- "_ is not a valid Win32 application"
- "This app can't run on your PC"
- "Your PC ran into a problem ... THis problem caused your PC to restart"
If core boot files become corrupted, then error messages may be:
- "Error loading operating system"
- "An error occurred while attempting to read the boot configuration data"
To fully detect, you must run an error checking utility, and if the drive has too many bad blocks, then it must be recycled.
Most drives have a built-in error correction code that periodically marks bad blocks in its internal error map (not the FAT table). This error map is only accessible with error checking utilities.
# Drive Death
Most drives are almost dead, but a fully dead drive will be undetectable to the OS. If it cant be detected by the BIOS or [[Windows Disk Management]], and it is not a power, data cable or motherboard jumper wire, then its safe to toss it in the bin.
# Power Cable Issues
Disconnect the drive data cable, but keep the power cable. If the drive spins up, then you know it is getting good power.
# [[ATA S.M.A.R.T]] software
- Used to check uptime of drive
- Used to check if drive is failing
- If imminent disk failure warning, replace disk
# HDD LED
- Should be intermittently flashing for normal operation
- Orange light means this hard drive has hardware issues
