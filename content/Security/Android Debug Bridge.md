---
tags:
  - android
  - reverse_engineering
aliases:
  - adb
---
A command line utility to allow for communication to an emulated android device.
Allows you to:
- Install apps
- Send commands to a shell
- Upload/Download files
# Installation (Arch)
1. `sudo pacman -S android-tools`
# Installation (Windows)
### Location
`C:\Users\Digit\AppData\Local\Android\Sdk\platform-tools`
# Commands
- `adb devices`
- `adb install <pathtoapkfile>` - installs an apk to the device
- `adb push <pathtofile>` - downloads a file to device
- `adb pull <pathtofile>` - downloads a file from device
- `adb shell` - opens a shell to the emulator where you can issue commands
- `adb connect <ip>` - connect to the emulator from a VM.
# Connect to emulator from VM (10.0.2.2)
10.0.2.2 on the emulated android device is equivalent to localhost on the host machine.
If you have a VM that can communicate to localhost, you can also communicate to this android device.
![[Android Virtual Device-20240901021713239.webp]]
You can use `adb connect 10.0.2.2` on the VM, and then you can communicate to the device.
![[Android Debug Bridge-20240901021925473.webp]]