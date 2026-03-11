---
tags:
  - nixos
---
A tool to update [[NixOS Packages|Nixpkgs]].
`nix flake update`
# Installatation
1. Configure the [[NixOS Configuration File]] and add the line:
   `nix.settings.experimental-features = [ "nix-command" "flakes" ];`
   ![[Flakes-20240827213608904.webp]]
2. `cd /etc/nixos`
3. `sudo nixos-rebuild switch`
4. `sudo nix flake init --template github:vimjoyer/flake-starter-config`. This will install a `flake.nix` file
5. The rebuild command will then be:
   `sudo nixos-rebuild switch --flake /etc/nixos#default`