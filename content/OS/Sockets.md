---
tags:
  - os
  - networking
---
A socket [[Point-to-point Communication|Full Duplex]] [[File Descriptor]] that acts an endpoint for network communication. 
Identified by [[IP Address]] + [[Port]]
- 2 processes want to communicate over a network ->  2 sockets are made.
# Socket Creation Process
1. Client initiates request for connection. It is assigned a random port greater than 1024
2. Server waits for client requests from specific port
3. Request is received
4. Server accepts connection from client
# Socket/Node programming
[https://www.youtube.com/watch?v=_FVvlJDQTxk](https://www.youtube.com/watch?v=_FVvlJDQTxk)

A method of two-way communication between 2 applications on the same network. It utilizes sockets/endpoint bound by port number on an ip so that the tcp layer can identify applications. A socket/endpoint is the combination of an ip address and port number.

Nodes are colloquial terms for devices. One node listens on a particular port of an ip while the other reaches out the instigate a connection.

  

We are responsible for programming socket commands that perform different actions depending on what signal another node sends. The following is the process:

**Socket creation**

socket.socket() - create a socket

socket.bind(host,port) - bind the socket to a host and a port

**Socket send. instigate**

socket.send() - send a signal

**Socket receiving process**

socket.listen() - constantly listen for a send signal

socket.recv() - received the signal and decode the message

**Socket closing**

socket.close() - close the socket