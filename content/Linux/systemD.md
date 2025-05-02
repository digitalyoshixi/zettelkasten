---
tags:
  - arch
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
# Creating Services
1. `vim /etc/systemd/system/myservice.service`
2. 
```c
[Unit]
Description=Serve site using npx serve
After=network.target

[Service]
Type=simple
WorkingDirectory=/path-to-work-with
ExecStart=/command-to-run
Restart=always
RestartSec=10
Environment=NODE_ENV=production

[Install]
WantedBy=multi-user.target
```
3. `sudo systemctl enable myservice.service`
4. `sudo systemctl start myservice.service`
### Creating Userland Services
1. `apt install dbus-user-session`
2. `mkdir -p ~/.config/systemd/user`