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
![[Pasted image 20230910191753.png]]
# [[OSI Model|OSI]] Formalities
- Communication on a serial line does not require a specific destination address, since the only address will the the device on the other line, though it is added for formality
- ISO standard HDLC does not have a type field. Cisco variants have a Type field.
  ![[High-Level Data Link Control Protocol-20250606012714558.webp]]
