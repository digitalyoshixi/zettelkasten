---
tags:
  - file_system
aliases:
  - NTFS
---
Window's preferred file system.
Uses clusters of blocks and file allocations tables like [[File Allocation Table Filesystem|FAT]] does, but improves on:
- Redundancy
- Security
- Compression
- Encryption
- Disk quota
- Smaller [[Cluster|Clusters]]
# Concepts
- [[Master File Table]]
- [[NTFS System Files]]
# Compression
NTFS can auto compress files when you need it to, however OS must decompress everytime it wants to access it which takes a lot of time
# Encryption
File encryption is possible with NTFS.
The microsoft utility for this is [[Microsoft EFS]]
# Disk Quotas
Ability for administrators to set limits on the drive space usage for users.
# Cluster Sizes
Cluser size varies depending on drive size.
![[NTFS-20240704031252006.webp]]
By default, NTFS supports up to 16TB, but if you tweak the cluser size, NTFS can work for up to 8 petabytes