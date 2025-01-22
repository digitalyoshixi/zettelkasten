---
tags:
  - nixos
  - ricing
---
# NVIDIA
1. First follow [[NixOS Nvidia Installation]]
2. edit `configuration.nix` and add the following: ![[NixOS Hyprland Installation-20240828024701337.webp]]
3. `sudo nixos-rebuild switch --flake /etc/nixos#default`
# AMD
1. Follow [[NixOS OpenGL Installation]]
2. Edit `configuration.nix`
```c
{ config, pkgs, ... }:

{
  security.polkit.enable = true;
  xdg.portal = {
    enable = true;
    extraPortals = [ pkgs.xdg-desktop-portal-hyprland ];
  };
  fonts.enableDefaultFonts = true;
  programs.dconf.enable = true;

  programs.hyprland = {
    enable = true;
    xwayland.enable = true;
  };
}

```
3. Edit `~/.config/hypr/hyprland.conf`
```c
env = WLR_DRM_DEVICES,/dev/dri/card1
```
4. Then follow https://www.youtube.com/watch?v=61wGzIv12Ds&t=360s