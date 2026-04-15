---
tags:
  - programming
  - c
  - networking
---
```c
int accept(int sockfd, struct sockaddr *cliaddr, socklen_t *addrlen);
```
- Reads from [[listen()]] queue, blocks new connections on listen
- Returns new descriptor for communication
- `cliaddr` stores address of client on return