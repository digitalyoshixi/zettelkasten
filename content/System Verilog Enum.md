---
tags:
  - verilog
  - programming
  - hardware
---
Creating a set of constants that are given their values from enumeration starting at 0
# Auto Incrementing
```verilog
enum {red, yellow, green} traffic_signal;
// int type -> red = 0, yellow = 1, green = 2
```
# Custom Enum Values
```verilog
enum {red=0, blue=2, green=6} Colors;
```