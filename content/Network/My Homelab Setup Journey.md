---
tags:
  - IT
  - projects
---
# Todo
- [x] Setup [[Proxmox ZFS Pool]]
- [x] Purchase a domain name and get the required certificate from ACME ✅ 2025-04-30
	- [ ] https://pve.proxmox.com/wiki/Renaming_a_PVE_node
	- [ ] https://forum.proxmox.com/threads/hostname-fqdn-huh.63667/
- [ ] Setup auto-patching of [[Proxmox]] OS 
- [ ] Run vulnerability scans with [[Greenbone]]
	- [ ] https://www.reddit.com/r/selfhosted/comments/1end5j6/advice_on_exposing_some_services_on_proxmox_to/
- [ ] Setup [[Load Balancer]] with [[nginx]]
- [x] Setup [[Linux Users]] with [[Principle of Least Privilege]]
- [x] Setup [[Proxmox]] [[Access Control Model|ACL]] ([[Software Firewall]])
# April 23 2025
- Setup old desktop to start running again, and plugged in:
	- 512GB [[Hard Drive|HDD]]
	- 8TB [[Hard Drive|HDD]]
- Realized that setting up any sort of [[Redundant Array of Independent Disks|RAID]] on the server would waste a ton of storage, since RAID only strips and mirrors from the smallest disk, which would mean 7.5TB are wasted.
- Watched this video: (https://inv.nadeko.net/watch?v=AP61_ETd2GE) on how to setup NAS on proxmox. Decided to use a [[Proxmox ZFS Pool]] to handle storage
- The domain FQDN must be left as invalid, since I dont have a certificate at this point in time. https://forum.proxmox.com/threads/hostname-fqdn-huh.63667/. I set mine as host1.invalid
- I finish the installation, and then access the webUI on my laptop
  ![[My Homelab Setup Journey-20250423202118991.webp]]
- To update the system to allow for the disk tab to be visible, we first:
	- Disable enterprise repos and enable non-subscription repos in the webui
	- We run this script: https://community-scripts.github.io/ProxmoxVE/scripts?id=post-pve-install
- The second disk that is 8T must be partitioned before proxmox is able to see it and attach it as storage
  https://forum.proxmox.com/threads/how-to-add-hard-drive-to-host.119376/ or https://inv.nadeko.net/watch?v=zIoDXWKsorg
	- I decided to use it as [[Proxmox LVM-Thin Storage]]
	- ![[My Homelab Setup Journey-20250423211456830.webp]]
	- ![[My Homelab Setup Journey-20250423210350703.webp]]
# April 25 2025
I setup [[Tailscale]]
# April 29 2025
Today i just bought a hostname
# April 30 2025
I renamed the hostname, forgot to backup and ruined my nodes. now i have to reinstall...
- Its ok though, we ended up adding everything back really quickly
- We setup [[Proxmox NGINX Guide|NGINX]]
- [[Dynamic DNS|DDNS]] with a porkbun script
- We also setup [[Proxmox Certificate Guide|Certificates]]
- Setup router port forwarding to lead to nginx's port 80 and 443
# March 1 2025
- I setup firewall rules for each node
# March 2 2025
- We need to setup CI/CD for each website that runs on my server (as i will update them constantly, especially the obsidian vault)
- I create a [[Github Runner]], and then create a [[systemD]] service to run it on startup
	- There is a specific technicality that github runner run.sh script must be ran as user, and LXC does not allow user services. So, we must edit the [[sudo|sudoers]] file to only allow the specific command `sudo systemctl restart mysite.service`
- create a [[systemD]] service to run the web app as the webrunner user