---
tags:
  - networking
aliases:
  - TCP
---
A [[Connection Oriented]] communication protocol that ensures **no data loss** in communication.
# Packet Structure
![[Transmission Control Protocol-20260318164940591.webp]]
# Protocol
![[Transmission Control Protocol-20250424163508860.webp]]
1. Device sends a request to get a packet of a certain TCP ID
2. Send TCP ID packet to device
3. Device replies with received
4. If the ID's have a gap, then one message was lost, the reciever asks for that lost message
# Additional Features
### Flow Control
Ability to limit the data sent 
# Concepts
- [[Three Way Handshake]]