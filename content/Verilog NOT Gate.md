---
tags:
  - verilog
  - programming
---
```verilog
module not_gate (
	input wire a,
	output wire not_gate
);
	assign not_gate = ~a;
endmodule
```