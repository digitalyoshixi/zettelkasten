---
tags:
  - os
  - file_system
aliases:
  - MFT
  - $MFT
---
An enhanced FAT table that exists in first chunks of the disc.
- Describes all files/folders on the volume
	- Timestamps
	- Stream names
	- List of cluster numbers where data streams reside
	- Security identifiers
	- File attributes
- MFT stored at root of NTFS partition
- A backup of the MFT exists in the middle of the disk.
# Forensic Analysis
- Can uncover information about file creation, modification, deletion
- Stored in root of NTFS partition (`C:\`) that can be acquired with [[Kroll Artifact Parser and Extractor|KAPE]]
# MFT Fields
- In use: if unchecked, its a deleted object
- Has Ads: Indicates if object contains [[Alternate Data Stream|ADS]]
# Exploring $MFT
- [[r-studio]]
- [[MFTECmd]]