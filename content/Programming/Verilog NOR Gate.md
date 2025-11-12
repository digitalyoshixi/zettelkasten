---
tags:
  - verilog
  - programming
---
```verilog
module nor_gate (
	input wire a,b,
	output wire nor_out
);
	assign nor_out = ~(a | b);
endmodule
```