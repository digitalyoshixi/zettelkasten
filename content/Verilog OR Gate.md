---
tags:
  - verilog
---
```verilog
module or_gate (
	input wire a,b,
	output wire or_out
);
	assign or_out = a | b;
endmodule
```