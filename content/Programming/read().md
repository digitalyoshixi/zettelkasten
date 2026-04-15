---
tags:
  - programming
  - os
aliases:
  - C read()
---
A syscall used for reading a file descriptor
```c
ssize_t read(int fd, void buf[count], size_t count)
```
# Example
```c
int fd = open("myfile.txt", O_RDWR);
char buff[1000];
int numread = read(fd, buff, 1000)
```
# Bin Exploitation
1. End your user input early with a null terminator and then hide your payload after the null terminator
2. Do not include a null terminator in your input and let the program read infinitely
