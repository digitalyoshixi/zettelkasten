---
tags:
  - programming
  - c
  - networking
aliases:
  - C recv()
---
```c
int recv(int socket, char *buff, int buff_len, int flags)
```
- Used to recieve message from a socket and write into [[Buffer]]
- Returns number of bytes recieved on success, -1 on error