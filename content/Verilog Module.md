---
tags:
  - verilog
  - hardware
  - programming
---
A representation of a [[Circuit]].
```verilog
module module_name(input1, input2, ..., output1, output2, ...);
	// logic
endmodule
```
# Example [[Half Adder]]
```verilog
module half_adder(input a,b, output sum,carry);    
	xor x1(sum, a, b);    
	and a1(carry, a, b);
endmodule
```