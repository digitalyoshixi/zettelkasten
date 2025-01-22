---
tags:
  - Arch
  - os
aliases:
  - systemctl
---
Linux's [[init]] system
# Install
`Sudo pacman -S systemd`
# Systemctl
Software to configure the system's [[Daemon Process|OS Service]] that run at startup.
- `systemctl enable service` to enable autostart of the service
- `systemctl disable service`
- `systemctl start service` runs the service
- `systemctl restart service` 