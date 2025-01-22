---
tags:
  - nixos
---
# Profiles
Creating different profiles for nixos configuration files.
![[NixOS Configurations-20240828021058787.webp|471]]
### Creation
1. Create a folder in `/etc/nixos` and put files required by the `configuration.nix`
2. Edit [[Flakes]] to have the new profile
   ![[NixOS Configurations-20240828021149351.webp]]
   # Modules
   These are specific .nix files for software or drivers.
   ![[NixOS Configurations-20240828022009206.webp]]