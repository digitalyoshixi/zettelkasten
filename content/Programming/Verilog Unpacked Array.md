---
tags:
  - programming
  - verilog
---
Requires dimensions after variable name
```verilog
logic [7:0] unpacked_data[4]; // 4 seperate 8-bit elements

unpacked_data[0] = 8'hDE;
unpacked_data[1] = 8'hAD;
unpacked_data[2] = 8'hBE;
unpacked_data[3] = 8'hEF;
```