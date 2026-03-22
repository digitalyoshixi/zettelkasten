---
tags:
  - networking
---
Used in [[Transmission Control Protocol|TCP]] establishing a [[Network Session|Session]] by transmitting an initial sequence number.
![[Three Way Handshake-20240816174930305.webp]]
Can be used to find which ports are open
# SYN
The client sends a synchronization packet.
This includes the initial sequence number of its next packet
# SYN-ACK
The server responds with and acknowledgement packet signifying the next expected packet the server wants
# ACK
The client responds with the acknowledgement packet to confirm this is the correct packet.
Then, a two way connection is formed.
# NACK
If the server does not recieve an ACK within a given timeframe, or recieves a NACK then this means there is an error in the expected headers.
# FIN
Sent to indicate no more data is to be sent
# FIN-ACK
Sent to respond to a FIN packet.
# RST
Used to terminate a session.
Always sent if talking to a closed port.
# RST-ACK
Sent to respond to RST packet.