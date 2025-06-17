---
tags:
  - verilog
---
```verilog
module mydesign ( input  x, y, z,     
                  output o);     
endmodule

module tb_top;
	wire [1:0]  a;
	wire        b, c;

	mydesign d0  (a[0], b, a[1], c); 
endmodule`
```