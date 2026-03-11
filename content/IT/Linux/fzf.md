---
tags:
  - linux
---
A fuzzy finder for linux shells
# Installation
1. 
```
   sudo pacman -S fzf
```
2. `vim .zshrc` and add:
```
source <(fzf --zsh)
```