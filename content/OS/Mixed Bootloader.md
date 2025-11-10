---
tags:
  - os
---
A [[Bootloader]] that bypasses the 512 byte bootloader limit by inserting 512-byte break in ASM code, making sure the rest of the loader is put after the boot sector.