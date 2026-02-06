---
tags:
  - os
---
# Installation
1. Ensure you have these mirrors in `/etc/pacman.conf`:
```
[core-debug]
Include = /etc/pacman.d/mirrorlist

[extra-debug]
Include = /etc/pacman.d/mirrorlist
```
2. 
```
sudo pacman -S glibc-debug
```