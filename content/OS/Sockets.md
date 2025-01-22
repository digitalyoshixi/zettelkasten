---
tags:
  - os
  - networking
---
A socket is an endpoint for communication. When 2 processes want to communicate over a network, 2 sockets are made.

The sockets are identified by IP address + port number

1. Client initiates request for connection. It is assigned a random port greater than 1024
    
2. Server waits for client requests from specific port
    
3. Request is received
    
4. Server accepts connection from client
    

The ports that the server waits for are well defined. Telnet is 23, ftp is 21, http is 80, ssh is 22. All ports from 1-1024 are well known.

packets(data) traveling between client and server are delivered to the appropriate port number.

By the way, you can have multiple clients connect to one server, they just all must have a different port.

### Socket/Node programming

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