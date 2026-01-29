---
tags:
  - arch
---
# Install .pacman file
`sudo pacman -U file.pacman`
# Enable Multilib Repository
1. `nvim /etc/pacman.conf`
2. uncomment 
   ![[Pacman-20241027205710231.webp]]
# Remove Package Lock
```
sudo rm /var/lib/pacman/db.lck
```
# Clear Package Cache
```
pacman -Sc
```