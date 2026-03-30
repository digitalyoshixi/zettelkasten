---
tags:
  - programming
  - c
aliases:
  - epoll_create()
  - epoll_ctl()
  - epoll_wait()
---
A collection [[Syscall]] to create and manage context in kernel.
- Creates a context using `epoll_create()`
- Add or remove [[File Descriptor]] to/from context using `epoll_ctl()`
- Wait for events in context using `epoll_wait()`
Can add/remove [[File Descriptor|FD]] while waiting. Uses a [[Red-Black Tree]] with $O(1)$ times. Only works on [[Linux]] systems.