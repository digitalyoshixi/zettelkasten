---
tags:
  - arch
---
# Installation
1. `sudo pacman -Syu`
2. `git clone https://aur.archlinux.org/yay.git`
3. `cd yay`
4. `makepkg -si`
# libalpm shared library failure to load
1. `sudo pacman -R yay-bin`
2. `sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si`