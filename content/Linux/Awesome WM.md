---
tags:
  - linux
  - ricing
---
awesome WM is the superior WM, its a mixed bag with DWM styled config, along with great defaults and lua language configurations.

# Terminology
##### Tags
![[Awesome WM-20231226202915855.webp]]

# Installation
1. `sudo pacman -S awesome xorg xorg-xinit`
2. `mkdir -p ~/.config/awesome/`
3. `cp /etc/xdg/awesome/rc.lua ~/.config/awesome/`
4. `cp /usr/share/awesome/themes/default ~/.config/awesome/themes`
5. edit your .xinitrc to include: `exec awesome`
6. `sudo pacman -S lxappearance`
7. `sudo pacman -S xterm`
8. `sudo pacman -S xdg-user-dirs`
Note: if network stops working, then just type `rfkill`
# Bundled Software
- [[wibar]]