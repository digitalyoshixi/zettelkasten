---
tags:
  - verilog
aliases:
  - Verilog Procedural Blocks
---
These are specific segments of procedural code that run given a condition.
Conditions include:
```verilog
always @(posedge clk) // rising edge
always @(negedge clk) // falling edge
always @(posedge clk or posedge rst) // multiple triggers
always @(*) // combinational (all inputs)
```