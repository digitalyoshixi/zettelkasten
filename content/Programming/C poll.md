---
tags:
  - programming
  - c
---
```c
int poll (strut pollfd *fds, unsigned int nfds, int timeout);
```
Where:
```c
struct pollfd{
	int fd;
	short events;
	short revents;
}
```