---
tags:
  - programming
  - c
aliases:
  - C fwrite()
---
```c
size_t fwrite(const void *ptr, size_t size, size_t n, FILE *stream)
```
- Writes `n` items of data, each `size` bytes long
- Returns number of items written