---
tags:
  - networking
aliases:
  - CAM Table
  - MAC Address Table
---
A table in [[Switch]] that maps [[Media Access Control Address|MAC Address]] to [[Network Interface]]
![[Content Addressable Memory Table-20260613152215195.webp]]
# Building CAM Table
1. Listen to incoming frames
2. If the frame's source MAC address is not in table, add its source MAC address mapped to the [[Network Interface]] it came from
![[Content Addressable Memory Table-20260613152912128.webp]]
# Pruning Table
- MAC addresses not used for 300 seconds are autoamtically removed