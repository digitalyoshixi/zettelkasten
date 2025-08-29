---
tags:
  - networking
aliases:
  - nc
---
A [[TCP & IP Model|TCP/IP]] swiss army knife.
- Used to connect to open ports
- Used to setup outbound connection
- Used for port scanning
# Connecting
```
nc ip port
```
```
nc domain port
```
# Listening
```
sudo nc -l -p 80
```