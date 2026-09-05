---
tags:
  - linux
---
A tool to change the monitor settings on [[Linux]]
# Change Brightnes
1. `sudo modprobe i2c-dev`
2. `sudo detect --verbose` to find the display number
3. `sudo ddcutil setvcp 10 50 --display 1`