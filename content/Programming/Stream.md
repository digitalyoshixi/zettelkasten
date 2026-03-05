---
tags:
  - os
aliases:
  - File Pointer
  - File Handle
  - File Stream
---
A method to interface [[File Descriptor]].
It describes a flow of data that is connected from a data source and arrives at a data destination. You are able to read or write to the stream.
# Structure
```c
struct stream{
	int fd;
	char* buffer;	
}
```
# Java
- A program that needs to read data needs a Input Stream or Reader
- A program that is writing data needs a Output Stream or Writer