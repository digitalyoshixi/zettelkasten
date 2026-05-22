---
tags:
  - networking
aliases:
  - CSMA/CA
  - CSMA/CD
---
A protocol to avoid data collision during communication caused by several devices communicating on one stream.
Used in [[Point-to-point Communication|Half Duplex]] or [[Hub|Repeater Hub]] networks.
# Protocol
1. Each channel is designated as either `idle` or `busy`
2. If the channel is `idle`, then data can be sent
### CSMA/CD
A fallback protocol as to what happens when data collisions will occur during CSMA. Used in early [[Point-to-point Communication|Half Duplex]] networks 
1. If a collision occurs, a jamming signal is sent to each devices that had a part in the collision
2. Each computer recieves jamming signal and waits a random amount of time before sending their data again
### CSMA/CA
Protocol for avoiding collisions altogether. Used in [[Wireless Local Area Network]] since, jamming signals cannot be sent as there is no cable to guarantee communication.
1. Detects if channel is idle
2. Wait a short period of time
3. Send data
4. Destination sends an ACK (acknowledgement) signal if they have received the data
5. If no ACK was received by the source device, then the entire process is restarted 
##### RTS/CTS
An optional protocol for CSMA that is slow but reliable.
1. Device sends a RTS (Ready to send) signal to the [[Access Point|WAP]]
2. [[Access Point|WAP]] halts all other communication at the first instance of idle traffic
3. [[Access Point|WAP]] responds with a CTS (Clear to send) signal to the sending device
4. Sending computer sends their data to [[Access Point|WAP]]