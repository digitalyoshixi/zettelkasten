---
tags:
  - arch
---
# Installation
https://github.com/korvahannu/arch-nvidia-drivers-installation-guide
### Installing Packages
1. Install [[yay package manager]]
2. Enable [[Pacman|multilib]] repository 
3. `sudo pacman -S nvidia`
4. `sudo pacman -S nvidia-utils`
5. `yay -S nvidia-settings`
### Setting Kernel Parameter
1. `sudo vim /etc/default/grub`
2. append `nvidia-drm.modeset=1` to the `GRUB_CMDLINE_LINUX_DEFAULT` line
3. `sudo grub-mkconfig -o /boot/grub/grub.cfg`
### Editing [[mkinitcpio]]
1. `sudo vim /etc/mkinitcpio.conf`
2. update the line `MODULES=()` to be:
```
MODULES=(nvidia nvidia_modeset nvidia_uvm nvidia_drm)
```
3. Update the like `HOOKS()` to remove the word `kms`
4. `sudo mkinitcpio -P`
### Editing Hook
1. `sudo pacman -S wget`
2. `wget https://raw.githubusercontent.com/korvahannu/arch-nvidia-drivers-installation-guide/main/nvidia.hook`
3. `sudo mkdir -p /etc/pacman.d/hooks/ && sudo mv ./nvidia.hook /etc/pacman.d/hooks/`
# Checking
1. `reboot`
2. `nvidia-smi`
# Installation for 1070 (or Pascal GPUs)
https://archlinux.org/news/nvidia-590-driver-drops-pascal-support-main-packages-switch-to-open-kernel-modules/