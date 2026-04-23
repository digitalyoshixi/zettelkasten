---
tags:
  - programming
  - c
  - networking
---
```c
int listen(int sockfd, int backlog)
```
- Allows the socket to start listening for connections
- Creates queue in kernel where a max of `backlog` connections wait to be accepted
Returns 0 on success, -1 on error