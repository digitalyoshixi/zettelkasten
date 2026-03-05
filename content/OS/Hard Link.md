---
tags:
  - os
---
An exact identical link of a given file.
- [[Inode]] is the same
- [[Inode]] will only be destroyed once all hard links are destroyed
```
ln <target> <name_of_link>
```
![[Hard Link-20260109155336140.webp]]
# Default Hardlinks
- By default, the [[Inode]] of a directory will have two links. One for the directory itself, and another for the `./` hard link
- Subdirectories will also point to this directory with their `../` hard link