---
tags:
  - security
  - linux
---
# Automatic
```
sudo pacman -S archlinux-keyring
```
# Manual
https://forum.manjaro.org/t/signature-is-invalid/94500/16
1. `sudo pacman -Scc`. answer `y` to everything
2. `sudo rm -r /etc/pacman.d/gnupg`
3. `sudo rm /usr/share/pacman/keyrings/*`
4. `sudo pacman-key --init`
5. `sudo pacman -Sy archlinux-keyring`
6. It is ok to have errors in that update. Just reply `Y`
7. `sudo pacman-key --lsign-key 02FD1C7A934E614545849F19A6234074498E9CEE`
8. `sudo pacman-key --list-keys` to see if keys are `[full]`
9. `sudo pacman -Sy archlinux-keyring`
10. `sudo pacman-key --list-keys`
11. `sudo pacman-key --init `
12. `sudo pacman-key --populate`
13. `sudo pacman-key --refresh-keys`. It is ok to have ALOT of errors here
