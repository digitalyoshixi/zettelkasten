---
tags:
  - programming
  - c
---
```c
int fseek(FILE *stream, long int offset, int whence)
```
The whence parameter is a enum:
- SEEK_SET : from beginning of file
- SEEK_CUR: from current file position
- SEEK_END: from end of file