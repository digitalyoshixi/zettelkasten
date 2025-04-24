---
tags:
  - data_layer
  - link_layer
  - networking
aliases:
  - PPP
---
One of the protocols used to for data transfer on serial lines. Similar to [[High-Level Data Link Control Protocol]] designed with routers and the [[TCP & IP Model]] model in mind, unlike the [[High-Level Data Link Control Protocol|HDLC]] which retconned those features in later.

https://www.ccnahub.com/ip-fundamentals/understanding-data-link-layer-encapsulation/
PPP has several functions useful for connecting 2 routers successfully.
- **Definition of a Header and Trailer:**  that allows delivery of a Data frame over the Link. _(Similar to other Data-Link Protocols such Ethernet Header and Trailer)_
- **Support for both Synchronous and Asynchronous link rates**. _(Symmetric or Asymmetric rates – good to for both: Home and Business users)._
- **A protocol Type field in the header:** allowing multiple Layer 3 protocols to pass over the same link such IPv4 and IPv6.
- **Built-in Authentication tools:** Password Authentication Protocol (PAP) and Challenge Handshake Authentication Protocol (CHAP)
- **Control protocols for each higher-layer protocol that rides over PPP:** allowing easier integration and support of those protocols.

## Encapsulation Frame
The frame looks as such:
![[Pasted image 20230910192432.png]]
The "Type" field, similar to its use case in [[High-Level Data Link Control Protocol|HDLC]], tells us if this packet belongs to a [[Internet Protocol|IPv4]]or [[IPv6]] address.

