---
tags:
  - programming
---
A [[Hardware Description Language|HDL]] that is:
- Weakly typed
- Concise
- Deterministic
- [[C]]-like
[[System Verilog]] is the better version of verilog.
# Installation/Setup
1. With [[VSCode]], install
   ![[Verilog-20250508023354797.webp]]
2. `yay -S iverilog`
3. `yay -S gtkwave`
# Simulating `.v` File
1. Write the `.v` file
2. `iverilog -o output.vpp input.v`
3. `vpp output.vpp`
4. `gtkwave output.vcd`
# Concepts
- [[Verilog Module]]
- [[Verilog Datatypes]]
- [[Verilog Operators]]
- [[Verilog Wire]]
# Boilerplate
```verilog
module module_name(){
	input A;
	output B;
	assign B = !A;
}
endmodule
```