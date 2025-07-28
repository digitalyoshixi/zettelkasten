---
tags:
  - os
aliases:
  - VM
---
A virtual machine is a disc image file, that contains the OS, software and files that can be ran on a [[Hypervisor]] client.
# Snapshotting
The ability to create snapshots of your system that can be restored.
Creating snapshots will impede performance, so it is recommended to not have many at once.
# Networking Options
![[Virtual Machine-20240723172626124.webp|438]]
- **Internal Network:** Allowing VM to communicate with other VM's on the hypervisor
- **Bridge:** Allowing the guest VM to share the same network as the host machine.
- **Virtual Network**: Create a [[Virtual Local Area Network|VLAN]] that only allows the guest VM to communicate with the host machine
- **Isolated:** Do not the VM have any networking
# Resource Allocation
It is recommended to allocate atleast:
- 4 GB RAM
- 50GB storage
CPU utilization varies on the type of server
# Concepts
- [[Virtualization Security]]