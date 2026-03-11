---
tags:
  - linux
  - os
---
![](file:///C:/Users/Digit/AppData/Local/Temp/lu17828v2iv72.tmp/lu17828v2ivs7_tmp_35736e9bcd21dd6e.png)

the most customizable shell.
# Set as Default Shell
1. `cat /etc/shells`
2. `chsh` and give `/bin/zsh`
3. `reboot`
# Configuration
### oh-my-zsh Installation
```
wget --no-check-certificate http://install.ohmyz.sh -O - | sh
```
### Themes
and then you can set the themes in `~/.zshrc`
And then write:
```bash
ZSH_THEME="jonathan"
```
All other themes are found in: https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
### Colors
zsh uses [[Xterm 256 Color Scheme]].
To change your color scheme, go into `~/.oh-my-zsh/themes/YOURTHEME` and then manually edit lines to change the color like such:
![[ZSH-20240713021119433.webp]]
# Fuzzy Finder
- [[fzf]]