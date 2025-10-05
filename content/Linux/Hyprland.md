---
tags:
  - arch
  - ricing
---
A [[Wayland]] based tiling window manager.
# Installation
### Nvidia Drivers
Follow this guide: [[NVIDIA Drivers Arch Linux Support]]
and then:
1. `sudo pacman -S egl-wayland`
2. `vim /etc/modprobe.d/nvidia.conf` and add the line:
```
options nvidia_drm modeset=1 fbdev=1
```
3. `vim ~/.config/hypr/hyprland.conf`
add the following lines:
```sh
env = LIBVA_DRIVER_NAME,nvidia
env = XDG_SESSION_TYPE,wayland
env = GBM_BACKEND,nvidia-drm
env = __GLX_VENDOR_LIBRARY_NAME,nvidia

cursor {
    no_hardware_cursors = true
}
```
4. `sudo mkinitcpio -P`
5. `Hyprland`
### Hyprland Setup Script
https://github.com/JaKooLit/Arch-Hyprland
1. `git clone --depth=1 https://github.com/JaKooLit/Arch-Hyprland.git ~/Arch-Hyprland`
2. `cd ~/Arch-Hyprland`
3. `chmod +x install.sh`
4. `vim install.sh` and comment out the line`execute_script "pipewire.sh"
5. `./install.sh`
##### Software Installed By This Script:
- [[swww]]
- [[ZSH]]
# Guides
- [[Hyprland Multiple Monitors]]
- [[Hyprland Multiple Monitor Wallpaper]]
- [[Hyprland Night Light Filter]]
- [[Hyprsome]]
- [[Hyprland Alt Tab]]
- [[Hyprland QT Platform]]