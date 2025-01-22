---
tags:
  - Arch
---
The arch linux package manager

# Update
`sudo pacman -Syu`
# Download Package from .pacman file
`sudo pacman -U muffon-2.0.2-linux-x64.pacman`
# Including Multilib
`vim /etc/pacman.conf`
And then uncomment the lines:
```
[multilib]
Include = /etc/pacman.d/mirrorlist
```
Then:
`sudo pacman -Sy`