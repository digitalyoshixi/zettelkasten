---
tags:
  - networking
aliases:
  - Packets
  - Frames
  - Messages
  - Packet
---
Messages are the data sent between computers. They are just bits of data passed around a cable, but they go by many names.
The [[OSI Model|OSI]] equivalent is the [[Protocol Data Unit|PDU]]
## Types
![[Pasted image 20230910172759.png]]
### Segment
Only used in the [[TCP & IP Transport Layer|Transport Layer]]. consists of a TCP header and the Data that includes an Application header(it is part of the data now) and the data.
### Packet
The most commonly used term for network messages. The [[TCP & IP Network Layer|Network Layer]] message. has your IP address header and your Data gotten from previous layers.
### Frame
The last encapsulated form of message before it enters the [[Bit Transmission]] of the [[TCP & IP Physical Layer|Physical Layer]].
They are messages that contain both header and trailer.
# Data
Its important to know that data not only includes the original data sent, but also the headers of the previous higher layers.
For example, this might be an example data on the IP layer:
`| SEQ5 | OK(200) | <div> "salutaions" <div> |
But, as you may notice, it is holding the headers of the previous [[TCP & IP Transport Layer|Transport Layer]] and [[TCP & IP Application Layer|Application Layer]]!!!

**This whole block containing the previous headers is called data, because the IP layer does not care about these headers**
