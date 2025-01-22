---
tags:
  - networking
---
A id assigned for services running on a device to allow for network communication.
# Port Types
![[Network Ports-20240729194646800.webp]]
### TCP or UDP
Depending on whether the service is using [[Transmission Control Protocol|TCP]] or [[User Datagram Protocol|UDP]] as communication, they can occupy different port spaces.
TCP port numbers are not the same as UDP port numbers.
This means you can have a service on TCP port 88 and a service on UDP port 88 and they will have different communication streams.
### Non-Ephemeral
Usually ports 0-1023. These ports are designated to be for specific services or protocols.
i.e only [[Hyper Text Transfer Protocol Secure|HTTPS]] should use port 443.
### Ephemeral/Temporary
Ports 1024-65535 used for temporary communication like when the client opens a communication stream to a non-ephemeral port on a server.
# Security
A [[Port Scanner]] can be used to determine all active ports.