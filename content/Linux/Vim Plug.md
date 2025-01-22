---
tags:
  - vim
---
https://github.com/junegunn/vim-plug

# Usage with nvim
1. download with the command:
```
sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs \
       https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```
2. go into your `~/.config/nvim/init.vim` and write the following:
```c
call plug#begin(stdpath('data') . '/plugged')
Plug "https://github.com/ThePrimeagen/vim-be-good" // this is a demo
call plug#end()
```
3. save your init.vim
4. open a new nvim, and then type in the command ```:PlugInstall```
5. updating is done with `:PlugUpdate`