---
tags:
  - verilog
  - programming
---
```verilog
module xnor_gate (
	input wire a,b,
	output wire xnor_out
);
	assign xnor_out = ~(a ^ b);
endmodule
```