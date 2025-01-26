---
tags:
  - networking
  - security
aliases:
  - ufw
  - Ubuntu Firewall
---
Firewall for ubuntu and debian
# Installation
1. `sudo apt install ufw`
### Policy Setting
1. `sudo ufw default deny incoming`
2. `sudo ufw default allow outgoing`
3. `sudo ufw enable`
# Allowing Ports/Services
You can either allow the service or the port
### Allowing ssh
`sudo ufw allow ssh`
OR
`sudo ufw allow 22`
# Disabling Firewall
`sudo ufw disable`
