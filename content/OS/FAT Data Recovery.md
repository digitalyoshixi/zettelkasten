---
tags:
  - forensics
  - file_system
---
# Idea
When files are removed:
- The directory entry will change the `0xE5` offset
- The [[File Allocation Table]] entries are reset to `0x00`
- All other aspects of the file remain
# Method
- Change the entry in the [[File Allocation Table]] from `0x00000000` to `0xFFFF FFF8` or `0xFFFF FF0F`
- Continue until you reach the next cluster
- Go to directory entry and replace the `0xE5` offset with another character, replace it with `_` or a `-`