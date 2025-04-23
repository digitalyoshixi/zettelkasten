---
tags:
  - virtualization
  - IT
---
This is quite a rudimentary firewall that is just an [[Access Control Model|ACL]].
# Layout
Every segment of this hierarchy of nodes will have its own firewall, and likewise inherit from the parent node.
![[Proxmox Firewall-20250423214159512.webp]]
# Adding Rules
https://inv.nadeko.net/watch?v=DNsLLrCgK0U
![[Proxmox Firewall-20250423214806849.webp]]
- vmbr0 is the standard interface that proxmox uses
- protocol is the specific protocol we are targetting
- Source is which IP the packets are coming from
- Macros are specific policies pre-made
	- SSH is a specific macro that allows SSH connection from specific source
	  ![[Proxmox Firewall-20250423215317852.webp]]