---
tags:
  - windows
  - security
---
# Profiles
Windows firewall allows for 3 different firewall profiles for 3 different network types.
### Domain Network
A windows network controlled by [[Windows Domain]] that runs [[Windows Active Directory]].
In this case, the domain server gives your device the firewall configuration
### Private Network
Enables:
- Resource sharing
- [[Network Discovery]]
### Guest Network
Disables all sharing and discovery
Windows will automatically ask if this network is private or public
![[Windows Firewall-20240726033116416.webp|504]]