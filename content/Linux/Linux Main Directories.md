---
tags:
  - linux
aliases:
  - Linux Directories
---
# /bin
Contains binaries and executables
# /sbin
Contains system binaries that should only be ran by the root user
# /lib
Shared code between binaries
# /usr
End user folder
### /usr/bin or /usr/sbin
Non-essential installed binaries
### /usr/local/bin
Binaries that you have locally compiled that wont conflict with those installed by a system package manager
# /etc
Editable text configurations
# /home
Stores user data with configurations and files
# /boot
Files required to boot the system
# /dev
Used to interface with devices and drivers
# /opt
Used for optional/add-on software. Rarely used
# /var
Variable files that will change as the operating system is being used
- Logs
- Cache files
# /tmp
Temporary files that will be cleared on system reboot
# /proc
Fake file-system created by linux kernel to keep track of running processes