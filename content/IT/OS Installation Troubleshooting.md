---
tags:
  - os
---
# Media Errors
- Bad USB or DVD
# No Boot Device Present
- Ensure boot order priority is the USB
- Check if USB is corrupted
# Graphical Mode Errors
- Hardware problems
- Driver problems
You can always continue to install and fix these later.
# Lockups During Installation
### Disc, Drive or Image Errors
These are commonly hardware problems
- Check drivers
- Run hardware diagnostics
### Log Files
There should be 20 installation phases, with each phase creating its own setuperr.log file.
Windows also creates its own setup.etl file in %WINDIR%/Panther which you can open with [[Windows Event Viewer]]\
# Continuous Reboots
- Document where is it rebooting. Is it at bios or at OS boot?
- F8 to boot from last known working configuration
- If system starts, disable automatic restarts in System Properties
  ![[OS Installation Troubleshooting-20240731193630811.webp|586]]
  this will allow [[Blue Screen of Death]] messages to appear
- Bad hardware
# Inaccurate System Date or Time
- Bad [[Complimentary Metal-Oxide Semiconductor Battery|CMOS]] battery
- 