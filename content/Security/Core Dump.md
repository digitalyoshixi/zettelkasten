---
tags:
  - reverse_engineering
  - programming
aliases:
  - Memory Dump
  - Crash Dump
  - Storage Dump
  - System Dump
  - ABEND Dump
  - Coredump
cssclasses:
---
A recorded state of program memory at a specific time generated when the program has **crashed**.

It includes:
- Register information
- Flags
# Generating Coredump
1. `sudo pacman -S gdb`
2. `pgrep -f firefox`, and save this PID
3. `sudo gdb -p <pid>`
4. in the gdb prompt, `generate-core-file` and then `quit`