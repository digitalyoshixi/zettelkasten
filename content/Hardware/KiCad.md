---
tags:
  - hardware
---
A [[Printed Circuit Board|PCB]] generating software.
It can create [[.gerber]] files
# Installation
```
sudo pacman -Syu kicad
sudo pacman -Syu --asdeps kicad-library kicad-library-3d
```
Note that when you run for the first time, this is the only time when you can load default symbols. If you dont have them, then uninstall packages and `rm -rf ~/.config/kicad`
# Guides
- [[KiCad Generating Gerber Files]]
- [[KiCad Loading Symbols]]
# Concepts
- [[Net]]
- [[Footprint]]
- [[Bill of Materials]]
- [[Ratsnest]]
- [[KiCad Project]]
- [[KiCad Schematic]]
# Resources
- https://thor.edu/storage/media/activities/1003/files/82872/Guide_to_PCB_design.pdf