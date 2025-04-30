---
tags:
  - virtualization
  - file_system
---
A file storage system that pools whenever writing instead of allocating blocks.
Allows for [[Storage Pools]].
# Adding Storage
- ![[My Homelab Setup Journey-20250423211456830.webp]]
- ![[My Homelab Setup Journey-20250423210350703.webp]]
# Removing Storage
1. `pvs` to find the drive you want to delete
2. `vgremove <drivename>`
3. Then, wipe the disk in the disks menu