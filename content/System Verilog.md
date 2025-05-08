---
tags:
  - verilog
  - programming
aliases:
  - sv
---
A [[Hardware Description Language|HDL]] that is similar in syntax to [[C]].
It is a better version of [[Verilog]] with:
- Improved data types
- [[Object Oriented Programming|OOP]]
- Assertions and coverage for function verification
# Simulating `.sv` File
1. Write `.sv` file
2. With [[Verilator]] installed, `verilator`
# Concepts
- [[System Verilog Module]]
- [[System Verilog Datatypes]]
- [[System Verilog Enum]]
- [[System Verilog Array]]
- [[System Verilog Dynamic Array]]
# Boilerplate
```verilog
module my_module;
	int array[];
	array = `{5,10,15,20,25};
	foreach (array[i])
	$display("hello");
	array.delete();
endmodule
```