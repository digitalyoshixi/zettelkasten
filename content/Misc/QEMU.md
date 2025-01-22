---
tags:
  - virtualization
---
A better version of Virtualbox and VMWare if you know what youre doing (which we do)

# Installation
### Windows
1. Installer from https://qemu.weilnetz.de/w64/2024/
2. Put `C:\Program Files\qemu` into [[Windows PATH]]
# Run A VM
Create an image with 
`qemu-img.exe create -f qcow2 mydisk.img 40G`
*will create a 40G qcow2 formatted disk*
`qemu-system-x86_64.exe -enable-kvm -cdrom YOURISO.iso -boot menu=on -drive file=mydisk.img -m 4G`
Will boot a x86_64 architecture from your ISO file on your mydisk with 4GB of ram
