---
tags:
  - nixos
  - linux
---
1. Edit `configuration.nix`
```c
{ config, pkgs, ... }:

{
  hardware.opengl = {
    enable = true;
    driSupport = true;
    driSupport32Bit = true;
  };
  
  services.xserver.videoDrivers = ["amdgpu"];
}
```
![[NixOS OpenGL Installation-20241029040459178.webp]]