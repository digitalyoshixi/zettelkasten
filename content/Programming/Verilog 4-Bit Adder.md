---
tags:
  - programming
  - verilog
---
```verilog
module four_bit_adder (
	input logic [3:0] a,
	input logic [3:0] b,
	input logic cin,
	output logic [3:0] sum,
	output logic cout
);
	always_comb
		{cout, sum} = a+b+cin;
endmodule
```