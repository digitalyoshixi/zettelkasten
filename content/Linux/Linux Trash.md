---
tags:
  - linux
---
heres how you can get a 'recycle bin' in linux.
Move the file into /tmp which will be cleared on system reboot
make an [[Shell Aliases|Alias]] `alias trash="mv -t /tmp"` but do it the alias way