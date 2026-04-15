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
# Socket Communication
![[Sockets-20260318164717046.webp]]

# Functions
- [[socket()]]
socket.socket() - create a socket
socket.bind(host,port) - bind the socket to a host and a port

**Socket send. instigate**

socket.send() - send a signal

**Socket receiving process**

socket.listen() - constantly listen for a send signal

socket.recv() - received the signal and decode the message

**Socket closing**

socket.close() - close the socket