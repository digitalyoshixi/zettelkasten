---
tags:
  - programming
aliases:
  - stat
  - Modified Access Creation
  - MAC
---
External data not relevant to the function of a file. Used to provide meta information
- Does NOT store [[File]] name ([[Directory]] stores this)
# Reading Metadata
```
stat ./filename
```
Uses the [[stat()]] [[Syscall]]
# Timestamps
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