---
tags:
  - programming
  - c
  - networking
---
```c
int connect(int socket, struct sockaddr *addr, int addr_len)
```
- Connects to an addres via socket, subsequent communication done over same socket fd
- Returns 0 on success, -1 on failure