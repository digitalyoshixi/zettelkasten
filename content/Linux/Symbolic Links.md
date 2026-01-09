---
tags:
  - os
aliases:
  - Soft Links
---
[[Link]] of a file at another location. 
Has a different [[Inode]]
```
sudo ln -s <target> <dest>
```
In the linux ricing scene, [[Dotfiles]] are symbolicly linked to real files, so that configurations are easy.
![[Symbolic Links-20260109155439990.webp]]
# Creating Link for New App
1. `sudo mv anki /usr/src/anki`
2. `sudo ln -s /usr/src/ank/anki /bin/anki`