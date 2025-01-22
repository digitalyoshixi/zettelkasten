---
tags:
  - linux
---
This all works (theoretically), it is preferred to install through the gnome graphical installer
https://nixos.org/manual/nixos/stable/#sec-installation
1. https://nixos.org/download/ download the minimal ISO and boot into it
2. `sudo -i`
3. `lsblk` to view drives
4. `fdisk /dev/sda` if sda is the drive you want to install on
5. `g`
6. new partition `n` with size of `+550M`
7. new partition `n` with all the remaining disk size
8. `w`
9. `mkfs.fat -F32 /dev/sda1`
10. `mkfs.ext4 /dev/sda2`
11. `mount /dev/sda2 /mnt`
12. `mkdir -p /dev/sda1 /mnt/boot`
13. `cd /mnt`
14. `nixos-generate-config --root /mnt`
15. `vim /mnt/etc/nixos/configuration.nix` and if you want to use grub as the default bootloader, set [`boot.loader.grub.device`](https://nixos.org/manual/nixos/stable/options#opt-boot.loader.grub.device) to `/dev/sda` and [`boot.loader.grub.efiSupport`](https://nixos.org/manual/nixos/stable/options#opt-boot.loader.grub.efiSupport) to `true`.
16. `nixos-install`
17. `reboot`
18. After reboot, `ln -s /etc/nixos /home/yoshixi/nixos`