---
tags:
  - programming
  - os
aliases:
  - Multiboot Header
---
A standard header that bootloaders check when searching for the kernel.
- Must be within the first 8KB of the kernel file
# Checking For Valid Header
```
grub-file --is-x86-multiboot myos'
echo $?
```
- 0 if header is found
- 1 if no header
