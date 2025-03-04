---
aliases: 
tags:
  - ricing
  - arch
---
1. `sudo pacman -S flameshot`
2. edit ~/.config/awesome/rc.lua
3. go to the line where keybinds are. add it after the menubar keybind if u want
4. paste in lines:
```
awful.key(
            {},
            "Print",
            function()
                awful.spawn("flameshot gui")
            end,
            {description = "flameshot gui", group = "awesome"}
        ),
        awful.key(
            {"Shift"},
            "Print",
            function()
                awful.spawn("flameshot gui -d 2000")
            end,
            {description = "flameshot gui with 2 second delay", group = "awesome"}
        )

```
