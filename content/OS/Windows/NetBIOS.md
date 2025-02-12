---
tags:
  - networking
  - windows
aliases:
  - nbtstat
---
An [[Application Program Interface|API]] for older windows systems that runs over [[Transmission Control Protocol|TCP]]/[[Internet Protocol|IP]] to allow network communication in a [[Local Area Network|LAN]].
Used to troubleshooting naming issues in networks.
- `udp/137`, `udp/138` used for name services (nbname)
- `tcp/139` used for session service (nbsession)
[[NetBT]] is the forward compatibility of NetBIOS on modern TCP/IP networks
# Commands
### `nbtstat -n`
Finding current device's netbios name
![[Windows nbtstat-20240718030043558.webp]]
### `nbtstat -A <remoteIP>`
Finding a remote IP's netbios name
![[Windows nbtstat-20240718030135909.webp]]
### `nbtstat -c`
All names NetBIOS has in its cache