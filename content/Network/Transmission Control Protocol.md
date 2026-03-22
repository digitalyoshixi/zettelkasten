---
tags:
  - networking
aliases:
  - TCP
---
A [[Connection Oriented]] communication protocol that ensures **no data loss** in communication.
![[Transmission Control Protocol-20250424163508860.webp]]
# Packet Structure
![[Transmission Control Protocol-20260318164940591.webp]]
- Source port: 16-bits, represents sending port
- Dest port: 16-bits, represents receiving port
- Sequence Number: 32-bits, used for keeping data in sequence
	- If SYN flag set (1), then this is initial sequence number
	- If SYN flag unset (0), this is accumulated sequence number
- Acknowledgement Number: 32-bits:
	- If ACK flag is set, this number is the next Sequence Number the sender expects
- Data Offset: 4-bits, specifies size of TCP header in 32-bit [[Binary|Words]]
- Reversed: 4-bits, never used
- CWR: 1-bit, used to indicate that congestion window has been reduced
- ECE: 1-bit
	- If SYN is set, TCP is [[Explicit Conjection Notification|ECN]] capable
	- if SYN is unset, signifies congestion or incoming congestion
- URG: 1-bit indicates that urgent pointer is significant
- ACK: 1-bit, indicates that acknowledgement fields are significant
- PSH: 1-bit, asks to push buffered data to receiving application
- RST: 1-bit, resets the connection
- SYN: 1-bit, used to synchronize sequence numbers
- FIN: 1-bit, used to signal this is the last packet from the sender
- Window: 16-bits, the size of the receive window that the sender is willing to recieve
- Checksum: 16-bits a [[Checksum]]
- Urgent Pointer: 16-bits: if set, indicates the offset from sequence number is the last urgent data byte
# Protocol
- SEQ: used to track bytes sent
- ACK: used to track bytes received
### [[Three Way Handshake]]
- Gets the initial sequence number (ISN)
### Communication
1. Alice sends packet with SEQ=ISN+1
2. Alice is able to continue sending until she reaches the window size specified by Bob
3. Bob after every second received packet. replies with acknowledgement: ACK=SEQ+data size+1
4. If the ACK does not match what alice should receive, receiver starts TCP retransmission
### Retransmission
- 
# Additional Features
### Flow Control
Ability to limit the data sent 
# Concepts
- [[Three Way Handshake]]
- [[Delayed Acknowledgement]]
- [[TCP WIndow Size]]
# Vulnerabilities
- [[Denial of Service|DoS]]
- [[Connection Hijacking]]
- [[TCP Veto]]
- [[Reset Attack]]