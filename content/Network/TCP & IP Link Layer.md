---
tags:
  - networking
  - link_layer
  - networking
aliases:
  - Link Layer
---
Defines protocols and hardware that is required for data transfer in physical networks. Link refers to the physical cable links between 2 devices.

The 5 layer [[TCP & IP Model|TCP/IP Model]] simply splits the link layer into its 2 functions of data transfer and physical media within the [[TCP & IP Data Layer]] and [[TCP & IP Physical Layer]].

Like all layers, the link layer provides services to the layer above it. Higher level layers like if the network layer wants to send something to another IP, it is the ethernet that manages how the packet maneuvers.

Networking diagrams often represent Ethernet as lines. Just simple lines.

### Ethernet Forwarding
ethernet forwarding can be broken down into 4 steps::
1. Our own computer [[Network/Encapsulation]] the packet inside an [[Ethernet Frame]] 
2. The packet is physically transmitted through electricity over Ethernet cabling
3. Router physically receives the electrical signal and re-creates the encapsulated packet through decoding the electrical signals
4. Router decapsulates the packet from the [[Ethernet Frame]]

Certain tasks in those 4 mentioned above within the 5 layer model are split between [[TCP & IP Data Layer]] and the [[TCP & IP Physical Layer]]. For example, Encapsulation and Addressing is a uniquely  [[TCP & IP Data Layer]] procedure. Likewise, Bit transmission is special to the [[TCP & IP Physical Layer]].
The link layer includes a large number of protocols and standards. For example: Ethernet protocols with other LAN standards like WAN.