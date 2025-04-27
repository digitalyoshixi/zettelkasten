---
tags:
  - IT
  - networking
---
A [[Virtual Private Network|VPN]] that jumps several times between dummy ISPs before making its way to the server.
# Setup
1. Ensure you have a tailscale account
2. `curl -fsSL https://tailscale.com/install.sh | sh`
3. `systemctl start tailscaled`
4. `tailscale up`
### LXC Setup
https://youtu.be/QJzjJozAYJo
### Proxmox Setup
1. `curl -fsSL https://tailscale.com/install.sh | sh`
2. `nano /etc/sysctl.conf` and uncomment these lines
   ![[Tailscale-20250427221912640.webp]]
3. `reboot`
4. Follow this guide:
	1. https://tailscale.com/kb/1320/performance-best-practices#ethtool-configuration
```
NETDEV=$(ip -o route get 8.8.8.8 | cut -f 5 -d " ")
sudo ethtool -K $NETDEV rx-udp-gro-forwarding on rx-gro-list off
printf '#!/bin/sh\n\nethtool -K %s rx-udp-gro-forwarding on rx-gro-list off \n' "$(ip -o route get 8.8.8.8 | cut -f 5 -d " ")" | sudo tee /etc/networkd-dispatcher/routable.d/50-tailscale
sudo chmod 755 /etc/networkd-dispatcher/routable.d/50-tailscale
sudo /etc/networkd-dispatcher/routable.d/50-tailscale
test $? -eq 0 || echo 'An error occurred.'
```
5. `tailscale up --advertise-routes=192.168.2.0/24 --advertise-exit-node`