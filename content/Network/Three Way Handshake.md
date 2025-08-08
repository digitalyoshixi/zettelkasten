---
tags:
  - networking
---
Used in [[Transmission Control Protocol|TCP]] for connection-oriented communication.
![[Three Way Handshake-20240816174930305.webp]]
Can be used to find which ports are open
# SYN
The client sends a synchronization packet.
This includes the sequence number of its next packet
# SYN-ACK
The server responds with and acknowledgement packet signifying the next expected packet the server wants
# ACK
The client responds with the acknowledgement packet to confirm this is the correct packet.
Then, a two way connection is formed.
# NACK
If the server does not recieve an ACK within a given timeframe, or recieves a NACK then this means there is an error in the expected headers.