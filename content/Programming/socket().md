---
tags:
  - programming
  - c
  - networking
aliases:
  - C socket()
---
```c
int socket(int family, int type, int protocol)
```
- `family` is [[UNIX Socket Families]]
- `type` is a [[UNIX Socket Connection Type]]
- `protocol` is set to protocol if [[SOCK_RAW]] is set
Will return a [[File Descriptor]] for the socket
# Example
```c
int tcpfd = socket(PF_INET, SOCK_STREAM, 0);
int udpfd = socket(PF_INET, SOCK_DGRAM, 0);
```
