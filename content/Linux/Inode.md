---
tags:
  - linux
---
A data structure that describes a file or directory. On the OS level.
- Last modified
- [[Metadata]]
- Parent
- Children
They are unique for a given filesystem.
A filesystem has a maximum of $2^{32}$ inodes
# Struct
- Size
- Owner [[UID]]
- Owner [[Group ID]]
- [[atime]], [[mtime]], [[ctime]]
- [[Link]] counts
- [[File Block|Block]] counts
- [[Permissions]]
- Direct pointer to [[File Block]]
- Single indirect pointers (actual file)
- Second indirect pointers (files in directory)
- Third indirect pointers (files out)
