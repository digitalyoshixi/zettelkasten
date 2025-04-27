---
tags:
  - networking
---
These are lightweight linux containers that run at near-native performance. They share the same kernel as the [[Hypervisor]].

For [[Proxmox]], these are usually the containers that run single services or programs.
# Security
Due to the shared kernel, LXCs are less secure, but you can run them unprivileged to
# Setup
1. `pveam available`
   ![[LXC-20250427200606792.webp]]
2. `pveam download local <disk_archive>`
   ![[LXC-20250427200800638.webp]]
3. Create a new LXC container
   ![[LXC-20250427201126410.webp]]
4. Select the template as the one previously created
   ![[LXC-20250427201209720.webp]]
5. ![[LXC-20250427201341318.webp]]
6. ![[LXC-20250427201502398.webp]]
7. ![[LXC-20250427201821683.webp]]
8. ![[LXC-20250427201845071.webp]]
9. ![[LXC-20250427201915214.webp]]
10. Afterwards, start the container and login
    ![[LXC-20250427202025447.webp]]
