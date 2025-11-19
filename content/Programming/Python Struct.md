---
tags:
  - python
---
A method to create [[C Structures]] in python, that converts python data into raw bytes.
# Boilerplate
```python
struct.pack(">HBH", 20, 0x4, 12)
```
# Format Types
| Format Code | Data Type       | Size (bytes) |
| ----------- | --------------- | ------------ |
| `b`         | Signed char     | 1            |
| `B`         | Unsigned char   | 1            |
| `h`         | Signed short    | 2            |
| `H`         | Unsigned short  | 2            |
| `i`         | Signed int      | 4            |
| `I`         | Unsigned int    | 4            |
| `f`         | Float           | 4            |
| `d`         | Double          | 8            |
| `Q`         | Unsigned Double | 8            |