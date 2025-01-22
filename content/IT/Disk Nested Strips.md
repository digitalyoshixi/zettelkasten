---
tags:
  - IT
aliases:
  - RAID 1+0
  - RAID 10
---
![[Disk Nested Strips-20240730205611244.webp]]
Requires 4 drives.
1. Make mirrors of 2 primary drives
2. Take the pair of mirrors and the pair of primary drives, and treats them as 2 'drives'.
3. [[Disk Striping]] implemented for the 2 'drives'
# RAID 10 Failure
Can lose all but one from each set of mirrors