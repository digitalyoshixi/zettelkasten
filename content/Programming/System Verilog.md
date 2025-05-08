---
tags:
  - verilog
  - programming
aliases:
  - sv
---
A [[Hardware Description Language|HDL]] that is similar in syntax to [[C]].
It is a superset of [[Verilog]] with:
- Improved data types
- [[Object Oriented Programming|OOP]]
- Assertions and coverage for function verification
# Simulating `.sv` File
1. Write `.sv` file
2. With [[Verilator]] installed:
```
verilator --binary -j 0 -Wall hello.sv
```
# Concepts
- [[Verilog Module]]
- [[System Verilog Datatypes]]
- [[System Verilog Enum]]
- [[System Verilog Array]]
- [[System Verilog Dynamic Array]]
- [[System Verilog Associative Array]]
- [[System Verilog Queue]]
# Boilerplate
```verilog
module my_module;
	initial
		int array[];
		array = `{5,10,15,20,25};
		foreach (array[i])
		$display("hello");
		array.delete();
endmodule
```