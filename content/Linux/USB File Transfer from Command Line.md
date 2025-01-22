---
tags:
  - networking
  - linux
---
1. get the usb drive's name. `lsblk`
2. make the mounting directory `sudo mkdir /media/usb`
3. `sudo mount /dev/sdb1 /media/usb`
4. if you need to then
. `sudo umount /media/usb`
