---
tags:
  - programming
  - c
aliases:
  - C select()
---
```c
int select(int nfds, fd_set *readfs, fd_set *writefds, fd_set *exceptfds, struct timeval *timeout);
```
- `nfds`: Number of [[File Descriptor|FDs]]
- `readfds`: is the [[Bitmap|Bitmask]] of [[File Descriptor|FDs]] we want to read
- `writefds`: is the [[Bitmap|Bitmask]] of [[File Descriptor|FDs]] we want to write
- `exceptfds`: is the [[Bitmap|Bitmask]] of [[File Descriptor|FDs]] for except conditionals of [[poll()]]
- `timeout`: time for timeout
- Returns the number of file descriptors returned in the 3 descriptor sets or -1 on error
- Updates readfs, writefs, exceptfs to only tick on files that are ready