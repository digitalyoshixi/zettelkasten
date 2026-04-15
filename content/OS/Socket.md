---
tags:
  - os
  - networking
---
A socket [[Point-to-point Communication|Full Duplex]] [[File Descriptor]] that acts an endpoint for network communication. 
Identified by [[IP Address]] + [[Port]]
- 2 processes want to communicate over a network ->  2 sockets are made
![[Sockets-20260318164613945.webp]]
# Socket Creation Process
1. Client initiates request for connection. It is assigned a random port greater than 1024
2. Server waits for client requests from specific port
3. Request is received
4. Server accepts connection from client
# UNIX Socket Communication
![[Sockets-20260318164717046.webp]]
# UNIX Functions
- [[socket()]]
- [[bind()]]
- [[listen()]]
- [[connect()]]
- [[accept()]]
- [[send()]]
- [[recv()]]
- [[close()]]
# Concepts
- [[UNIX Socket Families]]
- [[UNIX Socket Connection Type]]
