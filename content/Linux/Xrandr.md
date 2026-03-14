---
tags:
  - linux
---
Manages monitor positions

You may also consider installing xrandr along with arandr to assist with monitor positions, resolution and more.
`sudo pacman -S xorg-xrandr`
`sudo pacman -S arandr`
then run `arandr`
Find the perfect sweet spot, then create you xrandr command.
seperate each monitor with --output, and after each --output, list the specifications.
My example looks like this:
![[Awesome WM-20231022233532019.webp]]
`xrandr --output DP-1 --mode 1920x1080 --pos 0x0 --rotate normal --output HDMI-1 --mode 2560x1080 --pos 1920x0 --rotate normal -- output DVI-D-1 --mode 1920x1080 --pos 4480x0 --rotate normal`
Put it before you start the wm in .xinitrc