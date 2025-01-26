---
tags:
  - cpp
---
returns an integer of the memory size of the given variable or datatype enum.

# Example
```cpp
sizeof(bool) // will be one
```
This is the byte-size
```cpp
int x{};
sizeof(x) // 4 bytes
```

# Size Compendium
For unsigned:
```cpp
char  : 1 byte
short : 2 bytes
int   : 4 bytes
long  : 4 bytes
float : 4 bytes
double: 8 bytes
```
If its signed, then its going to be double the size.
