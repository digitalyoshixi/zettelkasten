---
tags:
  - programming
  - verilog
  - hardware
aliases:
  - System Verilog Hashmap
---
A [[Hashmap]] in verilog.
# Example
```verilog
module assoc_array();
	int num_cars[string]:
	initial begin
		num_cars = `{"hyundai" : 2, "suzuki" : 1, "tata" : 3};
		
```