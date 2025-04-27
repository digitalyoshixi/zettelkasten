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
