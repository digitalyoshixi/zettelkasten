---
tags:
  - networking
aliases:
  - C2
  - C2 Server
---
A server used by [[Threat Actor]] that serves as the center for issuing cyber attacks.
Allows bypassing of [[Endpoint Detection and Response|EDR]] software.
# Structure
![[Command and Control Server-20260507022435245.webp]]
1. [[C2 Implant]] that runs on target computer that is able to make contact with C2 and execute commands on the device
2. [[C2 Redirector]] server redirects requests to a appropriate server
3. [[C2 Listening Post]] to publish tasks and recieve results of those tasks
# Concepts
- [[C2 Implant]]
- [[C2 Redirector]]
- [[C2 Listening Post]]