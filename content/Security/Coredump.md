---
tags:
  - linux
  - debugging
---
# Generating Coredump
1. `sudo pacman -S gdb`
2. `pgrep -f firefox`, and save this PID
3. `sudo gdb -p <pid>`
4. in the gdb prompt, `generate-core-file` and then `quit`