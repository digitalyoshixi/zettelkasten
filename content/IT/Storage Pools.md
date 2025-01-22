---
tags:
  - partitioning
  - os
  - memory
aliases:
  - Storage Spaces
---
Turning multiple drives into one single storage pool.
# Creation
1. Open storage spaces tab in [[Windows Control Panel]]
2. Create a new storage space
   ![[Storage Pools-20240704042433258.webp]]
3. Select the drives you want to include in the pool
   ![[Storage Pools-20240704042505962.webp]]
# Storage Space Types
### Simple Spaces
Just pooled storage without any backup. If a single drive fails, all drives fail.
### Mirror Spaces
Using one drive as a mirror for the other. Literally just [[Disk Mirroring|RAID 1]]
