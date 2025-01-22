---
tags:
  - ricing
---
# Monitor Positions
`vim ~/.config/hypr/hyprland.conf`
type:
`hyprctl monitors all` to see all monitors names
And then write:
```
monitor=DP-3,1920x1080,0x0,1
monitor=HDMI-A-1,2560x1080,1920x0,1
monitor=DVI-D-1,1920x1080,4480x0,1
```
to have it arranged left to right.
# Workspace Compatibility
`vim ~/config/hypr/hyprland.conf`
You can write:
```
workspace=1,monitor:HDMI-A-1
workspace=2,monitor:DP-3
workspace=3,monitor:DVI-D-1
```