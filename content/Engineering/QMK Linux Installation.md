---
tags:
  - keyboards
  - linux
---
# Installation
1. `sudo pacman -S qmk`
2. `qmk setup`
3. `sudo cp /home/yoshixi/qmk_firmware/util/udev/50-qmk.rules /etc/udev/rules.d`
# Creating Firmware
1. `qmk compile -kb foostan/cornelius -km default`
2. `qmk config user.keyboard=foostan/cornelius`
3. `qmk new-keymap` with `foostan/cornelius`
4. Go to the directory. For example: `/home/david/qmk_firmware/keyboards/foostan/cornelius/keymaps/yoshixi`
5. edit `keymap.c` with a keymap layout from here: https://keymapdb.com/?keyCount=1-34 or create your own here: https://config.qmk.fm/#/foostan/cornelius/LAYOUT
6. Then, `qmk compile`