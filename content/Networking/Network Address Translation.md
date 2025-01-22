---
tags:
  - networking
aliases:
  - NAT
  - DNAT
---
Method of translating a set of IP addresses into another set of IP addresses
![[Network Address Translation-20240723022226038.webp|355]]
Since IPv4 addresses are limited, the [[Router]] will map several private IPs to a single public IP to create the illusion of a single public IPv4 address.
The router will then be able to translate:
- public ip for device > private ip for device
- private ip for device > public ip for device
# Obscurity
Since NAT only has one public IP, anyone outside the network will not be able to determine the devices within the network
# Dynamic NAT (DNAT)
Instead of mapping to just one public IP, NAT can map devices in a [[Local Area Network|LAN]] to a pool of public IPs purchased from the [[Internet Service Provider|ISP]].
This is better for speed.