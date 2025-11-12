---
tags:
  - verilog
  - programming
---
```verilog
module nand_gate (
	input wire a,b,
	output wire nand_out
);
	assign nand_out = ~(a & b);
endmodule
```