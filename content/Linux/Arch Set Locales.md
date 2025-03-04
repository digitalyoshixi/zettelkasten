---
tags:
  - arch
  - linux
---
1. Ensure the `/etc/locale.conf` is:
```
LANG=en_US.UTF-8
LC_CTYPE=en_US.UTF-8
```
2. `sudo pacman -S glibc-locales`
3. `sudo locale-gen`
4. `unset LANG`
5. `source /etc/profile.d/locale.sh`
6. Log out then log in again
Temp fix: `export LC_ALL="en_US.UTF-8"`