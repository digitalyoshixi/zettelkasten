---
tags:
  - hardware
---
Tool to create digital copies of documents.
# Scanner Types
- [[Flatbed Scanner]]
# Scanning Process
1. Install scanner's drivers
2. [[Gnu Image Manipulation Program|GIMP]] can scan images for you
3. Choose [[Technology Without an Interesting Name|TWAIN]] drivers
# Scanner Configuration
### Resolution
`lazer_focus x drum_turn_increment`
![[Scanner-20240725035218806.webp|603]]
All scanners support a native resolution called *optical resolution*.
A second resolution can be created through software upscaling.
2400 x 2400 dpi is recommended for most images.
[[Resolution Enhancement Technology]] makes better images, but increases image size
### Color Depth
Number of bits the scanner can use to describe each pixel.
Increasing color depth increases the number of colors available to scan.
### Grayscale Depth
How many shades of gray a scanner can see per pixel.
Recommended to be 16-bit
### Scan Speed
Scanners have a maximum scanning speed set by hardware.
The scanning speed will be determined by the other 3 settings.
# Network Scanning
Using the [[Server Message Block Protocol|SMB]] protocol for networking scanners so that other computers can use your scanner.