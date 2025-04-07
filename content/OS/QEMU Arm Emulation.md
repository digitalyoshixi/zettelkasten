---
tags:
  - virtualization
---
# Installation
1. 
```
sudo pacman -S qemu-system-arm
```
2. 
```
sudo pacman -S qemu-user-static
```
# Running
```
qemu-aarch64 -L /usr/aarch64-linux-gnu/ ./file_to_emulate
```
### Running on Port, then connecting with GDB
```
qemu-aarch64 -L -g 31338 /usr/aarch64-linux-gnu/ ./file_to_emulate
```
In gdb:
```
target remote localhost:31338
```
