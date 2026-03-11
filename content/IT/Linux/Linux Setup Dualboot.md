---
tags:
  - linux
---
Assumption:
1. Windows is previously installed
2. Linux is already installed
# Setup os-prober
1. `sudo su -`
2. `fdisk -l` and find the EFI System partition
3. `mount /dev/sda1`
4. `cd /`
5. `os-prober`
6. `grub-mkconfig -o /boot/grub/grub.cfg`