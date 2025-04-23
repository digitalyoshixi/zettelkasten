---
tags:
  - IT
---
# Todo
- [ ] Setup [[Proxmox ZFS Pool]]
- [ ] Purchase a domain name and get the required certificate from ACME
	- [ ] https://pve.proxmox.com/wiki/Renaming_a_PVE_node
	- [ ] https://forum.proxmox.com/threads/hostname-fqdn-huh.63667/
- [ ] Setup auto-patching of [[Proxmox]] OS 
- [ ] Setup [[Linux Users]] with [[Principle of Least Privilege]]
- [ ] Setup [[Software Firewall]]
# April 23 2025
- Setup old desktop to start running again, and plugged in:
	- 512GB [[Hard Drive|HDD]]
	- 8TB [[Hard Drive|HDD]]
- Realized that setting up any sort of [[Redundant Array of Independent Disks|RAID]] on the server would waste a ton of storage, since RAID only strips and mirrors from the smallest disk, which would mean 7.5TB are wasted.
- Watched this video: (https://inv.nadeko.net/watch?v=AP61_ETd2GE) on how to setup NAS on proxmox. Decided to use a [[Proxmox ZFS Pool]] to handle storage
- The domain FQDN must be left as invalid, since I dont have a certificate at this point in time. https://forum.proxmox.com/threads/hostname-fqdn-huh.63667/. I set mine as host1.invalid
- I finish the installation, and then access the webUI on my laptop
  ![[My Homelab Setup Journey-20250423202118991.webp]]
- The second disk that is 8T must be formatted before proxmox is able to see it and attach it as storage
- To update the system to allow for the disk tab to be visible, we first:
	- Disable enterprise repos and enable non-subscription repos in the webui
	- We run this script: https://community-scripts.github.io/ProxmoxVE/scripts?id=post-pve-install