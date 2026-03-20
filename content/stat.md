---
tags:
  - linux
  - os
---
A linux command used to read [[Metadata]]
- Linux metadata does NOT store [[File]] name ([[Directory]] stores this)
# Reading Metadata
```
stat ./filename
```
Uses the [[stat()]] [[Syscall]]
# Timestamps ([[Modified Access Creation]])
- Modified ([[mtime]])
- Accessed (Toggled by OS [[atime]] sometimes set off)
- Created ([[ctime]])
- Date Changed (MFT)
	- Updated after Inode modification
- Filename Date Created (MFT)
- Filename Date Modified (MFT)
- Filename Date Accessed (MFT)
- INDX Entry Date Created
- INDX Entry Date Modified
- INDX Entry Date Accessed
- INDX Entry Date Changed