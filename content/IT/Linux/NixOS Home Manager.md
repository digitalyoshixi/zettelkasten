---
tags:
  - nixos
---
A [[NixOS Module]] that is used to declaratively configure your home directory `~/.config` folder.
![[NixOS Home Manager-20240828015537685.webp]]
This effectively makes `configuration.nix` the only [[Dotfiles|Dotfile]] you ever need
# Installation (Root Level)
1. Add these lines to your [[Flakes]] file `flakes.nix`
   ![[NixOS Home Manager-20240828015249400.webp]]
2. Bring `inputs` parameter to `configuration.nix` function scope
   ![[NixOS Home Manager-20240828020436416.webp]]
3. Add these lines to `configuration.nix`
   ![[NixOS Home Manager-20240828015450835.webp|597]]
   ![[NixOS Home Manager-20240828015818631.webp|547]]
3. `nix run home-manager/master -- init && sudo cp ~/.config/home-manager/home.nix /etc/nixos`
4. Finally rebuild. `sudo nixos-rebuild switch --flake /etc/nixos#default`
You will now have a `home.nix` in `/etc/nixos/`
# Installation (Userland)
1. Add the package `pkgs.home-manager` to `configuration.nix`
   ![[NixOS Home Manager-20240828004519279.webp]]
2. `home-manager init`
# Updating Home-Manger
`home-manager switch`