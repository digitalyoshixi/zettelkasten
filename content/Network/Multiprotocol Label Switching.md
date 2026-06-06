---
tags:
  - networking
aliases:
  - MPLS
---
A [[Packet Switching|Packet Forwarding]] technology that works at [[OSI Data Layer|OSI Layer 2]].
- Used to forward data by labels rather than [[IP Address]] to create a shortest path
# Label
A 32-bit field inserted:
- Label value (20 bits) - actual label ID
- Traffic class (3 bits) - priority
- S (1 bit) - Marks last label in stack
- TTL (8 bits) - [[Time To Live]]
# Protocol
### [[Label Forwarding Information Base|LFIB]] Population
1. Each router creates 1-1 [[Network Session|Session]] with each of its neighbours
2. During this session, each exchange [[Label Forwarding Information Base|LFIB]], and add an entry to their local LFIB if they are missing a entry
	1. They add local label (highest label + 1) -> (their label, network interface, dest ip)
### Forwarding
![[Multiprotocol Label Switching-20260606002531798.webp]]
- First router pushes (creates the label of the path the packet goes through)
- All subsequent routers use previous label as an index to a [[Label Forwarding Information Base|LFIB]] and swap label (Forward and change label based off past label, no need to look at [[Routing Table]])
- Final router pops (removes the label and forwards to dest)