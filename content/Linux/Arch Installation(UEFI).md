---
tags:
  - arch
  - linux
---
https://www.youtube.com/watch?v=PQgyW10xD8s
### NTP
1. `timedatectl set-ntp true`
### Partitioning
1. `fdisk -l` find your drive
2. `fdisk /dev/yourdiskname`
3. `g` make a gpt label
4. `n` then `1` skip first sector, last sector `+550M` remove signature if required
5. `n` then `2` skip first sector, last sector is `+2G`. this is swap
6. `n` then `3` skip first sector, skip last sector. you have all the remaining space now
7. `t` then `1` to switch to partition `1` into EFI System
8. `t` then `19` to switch partition `2` into `swap`
9. `w`
10. `lsblk` find your boot and root drives
11. `mkfs.fat -F32 /dev/bootdrive`
12. `mkswap /dev/swapdrive`
13. `swapon /dev/swapdrive`
14. `mkfs.ext4 /dev/rootdrive`
15. `mount /dev/rootdrive /mnt`
16. `mkdir -p /mnt/boot/efi`
17. `mount /dev/bootdrive /mnt/boot/efi`
### Pacstrap
1. `sudo pacman -S archlinux-keyring`
2. `pacstrap /mnt base base-devel linux linux-firmware vim`

### FSTab
`genfstab -U /mnt >> /mnt/etc/fstab`

### Chroot
1. `arch-chroot /mnt /bin/bash`
2. `ln -sf /usr/share/zoneinfo/Canada/Eastern /etc/localtime`
3. `hwclock --systohc`

### Locale
1. `vim /etc/locale.gen`
2. uncomment these. ![[Arch Installation-20231201020651801.webp]] then :wq
3. `locale-gen`
4. make a new file `vim /etc/locale.conf`. write 
```
LANGUAGE=en_US.UTF-8
LC_ALL=en_US.UTF-8
LANG=en_US.UTF-8
```
### Hostname
change the hostname. usually its just `arch`
1. `vim /etc/hostname`
2. just write the name.

### Network Configuration
1. `vim /etc/hosts`
2. add in lines: 
```
127.0.0.1 localhost
::1 localhost
127.0.1.1 myhostname.localdomain myhostname
```
my host name is `arch` usually

### Root Password 
`passwd`

### Add users
1. `useradd -m david`
2. `passwd david`
3. `usermod -aG wheel,audio,video,optical,storage david`
4. `pacman -S sudo`
5. `visudo`
6. uncomment the line `%wheel ALL=(ALL:ALL) ALL`
7. add the line `Defaults !tty_tickets`

### Boot
1. `pacman -S networkmanager grub efibootmgr dosfstools os-prober mtools`
2. `systemctl enable NetworkManager`
3. `grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=grub_uefi --recheck`
4. `grub-mkconfig -o /boot/grub/grub.cfg`

### Cleanup
1.`exit`
2.`umount -R /mnt`
3.`reboot` remove the usb LIVE disk

# First boot
Seems I dont have internet. lets fix that
1. `systemctl restart NetworkManager`
# Prohibited [[Secure boot]]
If secure boot is enabled, then you must sign all of the grub software
- https://www.reddit.com/r/archlinux/comments/10pq74e/my_easy_method_for_setting_up_secure_boot_with/
- https://bbs.archlinux.org/viewtopic.php?id=282076
# Updating Keyring
- [[Pacman Updating Keyring]]
# Fixing Linux Kernel
1. `mount /dev/rootdrive /mnt`
	1. If the file system needs to be cleaned then do: `e2fsck -p /dev/rootdrive`
2. `mkdir -p /mnt/boot/efi`
3. `mount /dev/bootdrive /mnt/boot/efi`
4. `arch-chroot /mnt /bin/bash`
5. `sudo pacman -Syu linux`