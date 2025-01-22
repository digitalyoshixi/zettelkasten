---
tags:
  - nixos
aliases:
  - Nixpkgs
---
# Installing Packages
1. `vim /etc/nixos/configuration.nix`
2. Find packages at https://search.nixos.org/packages
3. Add the package name inside this list:
   ![[NixOS-20240827211429359.webp]]
4. `sudo nixos-rebuild switch`
### Package Cache
All packages are stored in `/nix/store`
![[NixOS-20240827211840164.webp]]
cached packages don't update automatically. Once installed, they stay the same version.
To update these packages, you must remove these packages
# List Of Current Packages
`nix-env -q`