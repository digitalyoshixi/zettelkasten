---
tags:
  - networking
---
A [[Scheduling Algorithm]] created by [[Domain Name Server|DNS]] server for use of a [[Load Balancer]].
Rotates request in ascending numerical order starting from lowest IP to highest, and forwards according to the current host it lands on.

This algorithm by itself is not able to detect the status of a server.G
