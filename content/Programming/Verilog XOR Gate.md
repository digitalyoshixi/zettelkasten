---
tags:
  - programming
  - verilog
---
```verilog
module xor_gate (
	input wire a,b,
	output wire xor_out
);
	assign xor_out = a ^ b;
endmodule
```