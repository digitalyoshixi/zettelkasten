---
tags:
  - networking
aliases:
  - Network Topologies
---
# Terminology
**Segment:** The connection between device and switch
# Topologies
### Point to point
![[Network Topology-20240716170132888.webp]]
2 computers are directly connected with a segment
### Bus
![[Network Topology-20240716170204816.webp]]
All devices are connected to a main cable with drop-down lines
Less cable is required but there is no redundancy when the main bus breaks
### Ring
![[Network Topology-20240716170404455.webp]]
Each device has two Point to Point connections to the devices beside them.
Data is forwarded via repeaters until it reaches its target device
### Star Topology
![[Network Topology-20240716165932864.webp]]
The switch connects to all devices.
Most common network topology
### Tree Topology
![[Network Topology-20240716170603208.webp|326]]
Hierarchical topology where the main bus branches off into star-topologies.
### Mesh Topology ([[Wifi Mesh Network]])
![[Network Topology-20240716170704327.webp]]
Every device on the network has a point-point connection with every other device on the network.
This means each device can function similarly to a router.
This is the fastest, but most expensive and most cluttered topology
### Hybrid
![[Network Topology-20240716170806644.webp]]
A combination of all previous topologies