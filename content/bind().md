---
tags:
  - programming
  - c
  - networking
aliases:
  - C socket bind()
  - socket bind()
  - C bind()
---
```c
int bind(int sockfd, const struct sockaddr *servaddr, socklen_t addrlen);
```
- Takes in the [[File Descriptor|FD]] created by [[socket()|C socket()]]
- Takes in a pointer to a [[sockaddr]] or struct:
- Binds the socket to specified address and port
Returns 0 on success, -1 on error