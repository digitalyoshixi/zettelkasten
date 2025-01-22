---
tags:
  - linux
---
The better version of [[Pulse Audio]] that works in [[Wayland]].

# Uninstall Pulse Audio
1. `pulseaudio --kill`
2. `sudo pacman -Rns pulseaudio`
# Install Pipewire
1. `sudo pacman -S pipewire pipewire-pulse wireplumber`
2. `systemctl enable --user pipewire`
3. `systemctl enable --user wireplumber`
4. `systemctl start --user pipewire`
5. `systemctl start --user wireplumber`
Also `sudo pacman -S pavucontrol` so you can have a GUI frontend to control sound.