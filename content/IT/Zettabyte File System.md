---
tags:
  - file_system
aliases:
  - ZFS
---
Developed for [[Solaris]].
Modern file system for linux servers. 
It acts as both the [[File System]] and the disk volume manager. Allowing it to have knowledge of both physical disks and their volumes.
# Data Protection
ZFS ensures data stored on discs cannot be lost due to:
- Physical errors
- [[Bit Rot]]
- [[Data Corruption]]
- Uses [[dnode]] instead of [[Inode]]
# Snapshots
ZFS has snapshot cloning which is one of its most powerful features