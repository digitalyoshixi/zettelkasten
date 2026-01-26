---
tags:
  - networking
  - linux
---
1. Get the usb drive's name. `lsblk`
2. Make the mounting directory `sudo mkdir /media/usb`
3. `sudo mount /dev/sdb1 /media/usb`
4. If you need to then: `sudo umount /media/usb`
