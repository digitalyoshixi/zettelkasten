---
tags:
  - programming
  - c
  - networking
aliases:
  - C send()
---
```c
int send(int socket, char *msg, int msg_len, int flags)
```
- Sends a message to a open socket
- Returns number of bytes sent on success, -1 on error