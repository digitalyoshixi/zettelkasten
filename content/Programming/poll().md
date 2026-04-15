---
tags:
  - programming
  - c
aliases:
  - C poll()
---
```c
int poll (struct pollfd *fds, unsigned int nfds, int timeout);
```
Where:
```c
struct pollfd{
	int fd; // actual fd
	short events; // events interested in
	short revents; // events that happened
}
```
- Updates fds pointer to point to a `nfds` size array of file descriptors
- Returns number of elements in fds whose `revents` field has been set to non-zero value. Returns -1 on error.
# Event Types
- `POLLIN`: data to be read
- `POLLPRI`: priority condition
- `POLLOUT`: writing is possible