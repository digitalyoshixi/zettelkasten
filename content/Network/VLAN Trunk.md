---
tags:
  - networking
aliases:
  - Trunking
  - Tagging
  - 802.1Q
  - VLAN Tagging
  - Multi Switch VLAN Setup
---
The ability to run [[Virtual Local Area Network|VLAN]] between multiple switches.
# Process
1. Packets will include the VLAN tag [[Network Messages|Header Frame]] for the VLAN ID during transmission

   ![[VLAN Trunk-20260704173151313.webp]]
2. Switch reads this VLAN tag, removes it, and forwards appropriately ([[Single Switch VLAN Setup]])
   ![[VLAN Trunk-20260704173300714.webp]]
# 802.1Q Format
802.1Q inserts a 4-byte VLAN header into the original frame's [[Ethernet Frame|Ethernet Header]]
- Inside the 4-byte VLAN header, there is a 12-bit VLAN ID used for identification
![[VLAN Trunk-20260704173518629.webp]]
