---
tags:
  - compression
  - programming
aliases:
  - FEC
---
Used in [[WebRTC]]
A optimization technique for [[User Datagram Protocol|UDP]] connection that sends a series of packets where each packet is [[Exclusive Or|XORed]] with the subsequent one, so that if data is corrupted, it can be restored with another XOR.