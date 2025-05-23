---
tags:
  - IT
aliases:
  - PBS
---
A [[Operating System|OS]] for automatic backups.
Easy to setup to connect to [[Proxmox|Proxmox VE]].
# Setup
1. Create a [[LXC]]
2. `wget https://enterprise.proxmox.com/debian/proxmox-release-bullseye.gpg -O /etc/apt/trusted.gpg.d/proxmox-release-bullseye.gpg`
3. `apt update && apt upgrade -y`
4. `apt install proxmox-backup`
