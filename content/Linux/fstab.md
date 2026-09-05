---
tags:
  - linux
---
A file `/etc/fstab` used to define how storage devices are mounted in the [[File System|Filesystem]].
# Mounting Disk to Directory
1. Get the disk [[Globally Unique Identifier|UUID]] by `blkid -o list`
2. Write to `/etc/fstab`
```
/dev/disk/by-uuid/<YOURUUID> <MOUNTDIRECTORY> ext4 defaults 0
```