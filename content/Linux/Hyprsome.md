---
tags:
  - ricing
---
https://github.com/sopa0/hyprsome
Software to allow for multiple workspaces for each monitor
# Setup
1. `cargo install hyprsome`
2. Add cargo to [[Linux PATH]]
3. `hyprctl monitors` to view the ids of monitors. ID 0 will span workspace 1-9, ID 1 will span 11-19, ID 2 will span 21-29, so on so forth.
4. Use [[wev]] to find keycodes for your keybinds
5. modify `~/.config/hypr/hyprland.conf` to allow for:
```c
  workspace=1,monitor:DP-1
  workspace=2,monitor:DP-1
  workspace=3,monitor:DP-1
  workspace=4,monitor:DP-1
  workspace=5,monitor:DP-1

  workspace=11,monitor:HDMI-A-1
  workspace=12,monitor:HDMI-A-1
  workspace=13,monitor:HDMI-A-1
  workspace=14,monitor:HDMI-A-1
  workspace=15,monitor:HDMI-A-1

bind=SUPER,1,exec,~/.cargo/bin/hyprsome workspace 1
bind=SUPER,2,exec,~/.cargo/bin/hyprsome workspace 2
bind=SUPER,3,exec,~/.cargo/bin/hyprsome workspace 3
bind=SUPER,4,exec,~/.cargo/bin/hyprsome workspace 4
bind=SUPER,5,exec,~/.cargo/bin/hyprsome workspace 5

bind=SUPERSHIFT,1,exec,~/.cargo/bin/hyprsome move 1
bind=SUPERSHIFT,2,exec,~/.cargo/bin/hyprsome move 2
bind=SUPERSHIFT,3,exec,~/.cargo/bin/hyprsome move 3
bind=SUPERSHIFT,4,exec,~/.cargo/bin/hyprsome move 4
bind=SUPERSHIFT,5,exec,~/.cargo/bin/hyprsome move 5

```