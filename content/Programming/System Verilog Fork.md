---
tags:
  - verilog
  - programming
  - hardware
---
Used to [[fork()]] a process.
# Example
```verilog
module fork;
	fork
		begin
			$display("hi");
		end

endmodule
```