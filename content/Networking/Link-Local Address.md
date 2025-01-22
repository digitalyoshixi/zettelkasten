---
tags:
  - networking
---
An [[IPv6]] address given to all devices upon boot, similar to [[Automatic Private IP Addressing]].
![[Link-Local Address-20240717162903332.webp|581]]
# Anatomy
### Link ID
The first 64 bits of Link Local Addresses are always: `fe80:0000:0000:0000`
### Interface ID
The last 64 bits of Link Local Address is a randomly generated number or an [[Extended Unique Identifier 64-bit|EUI-64]]
