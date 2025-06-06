---
tags:
  - networking
  - data_layer
  - link_layer
aliases:
  - HDLC
  - HDLC Protocol
---
A method used primarily for encapsulation on [[Leased Line|Serial Line]], along with [[Point-to-Point Protocol|PPP]].
Communication on a serial line does not require a specific destination address, since the only address will the the device on the other line, however,  [[High-Level Data Link Control Protocol|HDLC]] is designed for the OSI model, thus, in order for Cisco to fit it under TCP/IP model, they had to add a "Type" field that specifies whether this frame is for [[Internet Protocol|IPv4]] or [[IPv6]].
![[Pasted image 20230910191753.png]]
