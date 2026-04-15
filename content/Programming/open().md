---
tags:
  - programming
  - c
aliases:
  - C open()
  - C open
---
```c
int open(const char *path, int flags, int mode)
```
- Returns the [[File Descriptor|FD]] of the opened file
- `mode` only in use depending on flags
# Example
```c
int fd = open("sample.txt", O_RDWR | O_CREAT, 0644); // read write, and create if not already created
```