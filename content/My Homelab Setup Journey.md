---
tags:
  - IT
---
# Todo
- [ ] Setup [[Proxmox ZFS Pool]]
- [ ] Purchase a domain name and get the required certificate from ACME
# April 23 2025
- Setup old desktop to start running again, and plugged in:
	- 512GB [[Hard Drive|HDD]]
	- 8TB [[Hard Drive|HDD]]
- Realized that setting up any sort of [[Redundant Array of Independent Disks|RAID]] on the server would waste a ton of storage, since RAID only strips and mirrors from the smallest disk, which would mean 7.5TB are wasted.
- Watched this video: (https://inv.nadeko.net/watch?v=AP61_ETd2GE) on how to setup NAS on proxmox. Decided to use a [[Proxmox ZFS Pool]] to handle storage
- The domain FQDN must be left as invalid, since I dont have a certificate at this point in time. https://forum.proxmox.com/threads/hostname-fqdn-huh.63667/