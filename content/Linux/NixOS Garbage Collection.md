---
tags:
  - nixos
---
Removing cached packages.
`sudo nix-collect-garbage --delete-older-than 15d` will delete packages older than 15 days