---
tags:
  - linux
---
# Setup Process
1. `sudo pacman -S bluez`
2. `sudo pacman -S bluez-utils`
3. `sudo systemctl enable bluetooth`
4. `sudo systemctl start bluetooth`
5. `sudo pacman -S blueman`
6. `bluetooth-manager`