---
tags:
  - networking
---
The logic that a [[Switch]] uses to forward messages when connected to other switches in a connected [[Local Area Network|LAN]].
![[LAN Switching-20260613151534554.webp|412]]
# Logic
1. Check packet MAC address
2. Find corresponding [[Network Interface]] from [[Content Addressable Memory Table|CAM Table]]
3. If the target network interface is different from the network interface that issued the frame, forward
4. If the target network interface is the same from the network interface that issued the frame, filter (don't send)
5. If there is no entry in table, forward frame out of all interfaces except receiving interface with [[Spanning Tree Protocol]] (Flood)
