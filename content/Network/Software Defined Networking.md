---
tags:
  - networking
aliases:
  - SDN
---
An approach to network management that creates software versions of network devices
# Planes
Diving up each networking device functionality into 3 planes for software implementation.
### Infrastructure Layer / Data Plane
Responsible for all processing of frames and packets like:
- Forwarding
- Trunking
- Encryption
- [[Network Address Translation|NAT]]
### Control Layer / Control Plane
For the control of these packets like:
- Routing tables
- Session tables
- [[Network Address Translation|NAT]] tables
### Application Layer / Management Plane
Ability to access each device:
- SSH
- Browser
- API
- [[Simple Network Management Protocol|SNMP]]