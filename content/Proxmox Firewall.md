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
![[Proxmox Firewall-20250423214806849.webp]]
- vmbr0 is the standard interface that proxmox uses