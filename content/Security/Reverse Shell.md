---
tags:
  - security
---
This [[Malware]] that opens a port on the targets device exposing a shell process.
# Process
1. Target opens up a port for a `/bin/sh`
2. Attacker uses [[Netcat|nc]] to connect to that open port
# Methods
 - [[Reverse SSH Tunnel]]