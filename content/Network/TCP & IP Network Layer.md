---
tags:
  - networking
  - networking
  - networking
aliases:
  - Network Layer
---
The Network layer only has 1 protocol worth mentioning, and that is the [[Internet Protocol]]

The IP layer is what allows for addressing. There are 2 forms the IP layer takes on. That is IPv4 and IPv6.

## Encapsulation Protocols
Encapsulation on the Network layer, unlike [[TCP & IP Data Layer|Data Layer]] Encapsulation, is not restricted to the specific hardware it is on. All the IP is, is just a method of addressing a specific device, so it would not make sense to base it off any specific hardware.
Thus, Each device can use either of these Encapsulation methods: [[Internet Protocol|IPv4]] and [[IPv6]]

IPv4 and [[IPv6]] have different methods of encapsulation of packets. This is stemmed from the fact that [[IPv4]] and [[IPv6]] have different methods of writing IP addresses.

For example, IPv4 has 256^4 possible IP address combinations. \*\.\*\.\*\.\* they are 32bit addresses

IPv6 can have around 79228162514264337593543950336 possible IP address combinations. Each Ip address is stored in hex and divided 4\*8 format. 
And example IPv6 can look like this:
![[Pasted image 20230910183918.png]]

