---
tags:
  - IT
aliases:
  - PBS
---
A [[IT/Operating System|OS]] for automatic backups.
Easy to setup to connect to [[Proxmox|Proxmox VE]].
# Setup
1. Create a [[LXC]] with turnkey-core [[Proxmox Template]]
2. `wget https://enterprise.proxmox.com/debian/proxmox-release-bullseye.gpg -O /etc/apt/trusted.gpg.d/proxmox-release-bullseye.gpg`
3. Edit `/etc/apt/sources.list` with:
```
deb http://deb.debian.org/debian bookworm main contrib
deb http://deb.debian.org/debian bookworm-updates main contrib

# Proxmox Backup Server pbs-no-subscription repository provided by proxmox.com,
# NOT recommended for production use
deb http://download.proxmox.com/debian/pbs bookworm pbs-no-subscription

# security updates
deb http://security.debian.org/debian-security bookworm-security main contrib
```
4. `apt update && apt upgrade -y`
5. `apt install proxmox-backup`
6. The backup webui is now visible at: `https://{container ip}:8007`
