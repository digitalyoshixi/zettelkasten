---
tags:
  - linux
  - c
---
A dynamic memory leak finding tool for [[Linux]] devices.
# Usage
```
valgrind --show-leak-kinds=all --leak-check=full ./myfile args
```