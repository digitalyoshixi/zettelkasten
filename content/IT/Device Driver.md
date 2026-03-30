---
tags:
  - os
aliases:
  - Drivers
---
Device drivers allow the CPU to communicate with proprietary peripheral devices.
They store the translations to all commands that the device may send.
# Viewing Drivers
- [[Windows Device Manager]]
- Can be mapped at `\Device\PhysicalMemory`
# Unsigned Drivers
Windows has a hardware compatibility program for drivers that work with their OS. By default, windows does not enable drivers that do not have the [[Digital Signature]]. You can still use them though, you just need to enable them.
# Beta Drivers
Drivers that are latest version and untested. They can cause immense system instability.