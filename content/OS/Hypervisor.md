---
tags:
  - virtualization
---
A program designated to control and allocate hardware among several operating systems.
![[Hypervisor-20240723170307086.webp|393]]
# Kernel Technologies
- [[VT-x]]
- [[AMD-V]]
# Types
![[Hypervisor-20240723174108223.webp|301]]
### Type-1
Bare-metal hypervisors.
There is no software between it and the hardware.
Used primarily in servers.
### Type-2
Hypervisors that run on top of an [[IT/Operating System|OS]]
##### Implementations
- [[Kernel Virtual Machine]]
- [[Hyper-V]]
- [[VirtualBox]]
- [[VMWare]]
# Security
- [[Hypervisor Security]]