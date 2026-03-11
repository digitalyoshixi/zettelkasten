---
tags:
  - bash
  - linux
---
# Regular aliasing
`alias --save trash="mv -t /tmp`
# .bashrc aliasing
1. `vim ~/.bashrc`
2. add your alias. example: `alias cppcompile="./~/Documents/cppcompile.sh"`
3. save file, source bashrc. `sh` then `source ~/bashrc` OR `. ~/bashrc`

This DOES NOT WORK WITH non-[[POSIX]] compatible terminals like [[Fish]]