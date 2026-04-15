---
tags:
  - programming
  - c
  - networking
aliases:
  - sockaddr_in
---
# sockaddr
```c
struct sockaddr{
	short sa_family;
	char sa_data[];
}
```
# sockaddr_in
```c
struct sockaddr_in {
	short sin_family; // AF_INET
	in_port_t sin_port;
	struct in_addr sin_addr;
}
```