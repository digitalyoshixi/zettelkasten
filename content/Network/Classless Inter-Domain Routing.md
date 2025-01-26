---
tags:
  - networking
aliases:
  - CIDR
---
A method of dividing [[IPv4]] addresses into classes.
# Overview

| Class                         | Most-significant bits | Network prefix size (bits) | Host identifier size (bits) | Address range             |
| ----------------------------- | --------------------- | -------------------------- | --------------------------- | ------------------------- |
| A                             | 0                     | 8                          | 24                          | 0.0.0.0–127.255.255.255   |
| B                             | 10                    | 16                         | 16                          | 128.0.0.0–191.255.255.255 |
| C                             | 110                   | 24                         | 8                           | 192.0.0.0–223.255.255.255 |
| D(multicast)  <br>E(reserved) | 1110  <br>1111        | –                          | –                           | 224.0.0.0–255.255.255.255 |
# Classes
https://www.meridianoutpost.com/resources/articles/IP-classes.php
### Class A
![[Classless Inter-Domain Routing-20240731030507319.webp|348]]
- Subnet Mask `255.0.0.0`
- Network ID first octet
- Host ID last 3 octets
- Public IP range `0.0.0.0 - 127.255.255.255` 
- Private IP range `10.0.0.0 - 10.255.255.255` or `10.*.*.*`
### Class B
![[Classless Inter-Domain Routing-20240731030620443.webp|338]]
- Subnet Mask `255.255.0.0`
- Network ID first 2 octets
- Host ID last 2 octets
- Public IP range `128.0.0.0 - 191.255.0.0`
- Private IP range `172.16.0.0 - 172.31.255.255` or `172.16-31.*.*`

### Class C
![[Classless Inter-Domain Routing-20240731030903377.webp|334]]
- Subnet Mask `255.255.255.0`
- Network ID first 3 octets
- Host ID last octet
- Public IP range `192.0.0.0 - 223.255.255.0`
- Private IP range `192.168.0.0-192.168.255.255` or `192.168.*.*`
- Special [[Loopback]] IP range `127.0.0.0 - 127.255.255.255` or `127.*.*.*`
