---
tags:
  - verilog
  - programming
aliases:
  - Verilog Fixed-Size Array
---
Syntax is size before variable name
```verilog
logic [3:0][7:0] packed_data;    // 32 bits total, stored as one chunk

// Assign all at once as a single 32-bit value
packed_data = 32'hDEADBEEF;

// Access individual bytes
// packed_data[3] = 0xDE
// packed_data[2] = 0xAD
// packed_data[1] = 0xBE
// packed_data[0] = 0xEF

// Can also treat it as one big 32-bit value
// packed_data = 0xDEADBEEF
```