---
tags:
  - verilog
aliases:
  - Verilog Continuous Assignment
  - Verilog Procedural Assignment
  - Verilog Blocking Assignment
  - Verilog Non-Blocking Assignment
---
# Updating Types
### Continuous Assignment
Assigns a net/variable continuously.
Models from [[Verilog Combinational Sequence]].
```verilog
assign y = a & b // continuous (combinational)
```
### Procedural Assignment
Assigning once, must be done within an always block
```verilog
always_comb z = x+1 // procedural, combinational
always_ff @(posedge clk) q <= d // procedural, sequential
```
# Blocking Types
### Blocking
```verilog
always @(...) out = in1 & in2 // blocking (combinational)
```
### Non-Blocking
```verilog
always @(...) out <= in1 & in2 // non-blocking (sequential)
```