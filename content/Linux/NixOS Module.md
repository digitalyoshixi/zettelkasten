---
tags:
  - nixos
---
Another .nix file that can be included within the main `configuration.nix`
# Sourcing Modules
Within the imports section, add your nix file
![[NixOS Modules-20240827234317015.webp]]
# Module Options
These are parameters inside one module that can be changed by other .nix modules.
![[NixOS Modules-20240827234454164.webp]]
There will occasionally be a default value for these options.