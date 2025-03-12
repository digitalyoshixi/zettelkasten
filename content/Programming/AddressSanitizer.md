---
tags:
  - linux
---
This is a package already installed with [[GCC]]
# Compiling With Address Sanitize
```c
gcc -g -O0 -fsanitize=address,undefined -fno-omit-frame-pointer <your_code>
```