---
tags:
  - os
---
symbolic links are links of 1 file that refer to another file location. maybe think of it like a shortcut for windows.
`sudo ln -s /../../targetdir /../../destinationdir`
In the linux ricing scene, [[Dotfiles]] are symbolicly linked to real files, so that configurations are easy.
# Creating Link for New App
1. `sudo mv anki /usr/src/anki`
2. `sudo ln -s /usr/src/ank/anki /bin/anki`