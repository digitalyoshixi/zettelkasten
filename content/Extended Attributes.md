---
tags:
  - os
  - forensics
aliases:
  - xattr
  - setfattr
---
Custom [[Metadata]] fields within a [[File System|Filesystem]] (commonly [[Fourth Extended File System|ext4]])
# Setting Attributes
```
setfattr --name=user.checksum --value="3baf9ebce4c664ca8d9e5f6314fb47fb" file.txt
```
# Getting Attributes
```
getfattr --encoding=text --dump file.txt
```