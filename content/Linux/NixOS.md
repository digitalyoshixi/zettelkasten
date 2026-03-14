---
tags:
  - libre
  - nixos
---
![[NixOS-20240827212609221.webp|194]]
A operating system based off the ethos of replicability and stability
# Rebuild Command
### Local
`sudo nixos rebuild switch`
### Full
`sudo nixos-rebuild switch --flake /etc/nixos#default`
If you have different [[NixOS Configurations]], then change `#default` to that other configuration
![[NixOS-20240828021021862.webp]]
# Concepts
- [[NixOS Configuration File]]
- [[NixOS Installation]]
- [[NixOS Packages]]
- [[NixOS Garbage Collection]]
- [[Flakes]]
- [[NixOS Module]]
- [[NixOS Home Manager]]
- [[Nix]]
### Software Installations
- [[NixOS Nvidia Installation]]
- [[NixOS OpenGL Installation]]
- [[NixOS Hyprland Installation]]
### [[Wayland]] tools