---
tags:
  - networking
aliases:
  - LSP
  - Link State Advertisement
  - LSA
  - LSDB
---
A protocol used to share [[Routing Table]] to all neighbors in a network
# Protocol
- Each router sends Link state advertisements that contain:
	- Router
	- Network information
	- Subnet information
- Routers aggregate this into a Link State Database which is a [[Graph Database]]