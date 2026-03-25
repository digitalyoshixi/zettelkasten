---
tags:
  - programming
  - c
---
```c
int select(int nfds, fd_set *readfs, fd_set *writefds, fd_set *exceptfds, struct timeval *timeout);
```
- `nfds`: Number of [[File Descriptor]]
- `readfs`: is the [[Bitmap|Bitmask]] we use for file descriptors
- `writefs`: is the [[Bitmap|Bitmask]] we use for file descriptors
- `except`: is the [[Bitmap|Bitmask]] we use for file descriptors
- `timeout`: time for timeout