---
tags:
  - verilog
  - programming
---
Arrays that are stored to be able to combine [[Verilog Unpacked Array]] and [[Verilog Packed Array]]
```verilog
logic [7:0] memory[0:3];         // 4 addresses, each holding 8 bits

// Assign like unpacked (address-by-address)
memory[0] = 8'hDE;
memory[1] = 8'hAD;
memory[2] = 8'hBE;
memory[3] = 8'hEF;

// Access by address
// memory[0] = 0xDE
// memory[1] = 0xAD
// memory[2] = 0xBE
// memory[3] = 0xEF
```