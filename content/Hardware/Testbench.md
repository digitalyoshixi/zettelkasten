---
tags:
  - hardware
  - programming
---
A test for [[Field Programmable Gate Arrays|FPGA]] behavior written in [[System Verilog]].
Involves coverage and test cases.
# Example Test Bench Creation
1. Create the verilog module:
```verilog
module andprogram(
    input reg a,
    input reg b,
    output reg c
    );
    assign c = a & b;
endmodule
```
2. Create the test bench:
```verilog
`timescale 1ns / 1ps

module andtest();
    logic [1:0] mySW;
    logic myOut;
    
    andprogram module_under_test(mySW[1], mySW[0], myOut);
    
    initial begin
        #100 mySW = 2'b00;
        #100 mySW = 2'b01;
        #100 mySW = 2'b10;
        #100 mySW = 2'b11;
    end
endmodule
```
3. Project structure looks like this:
![[Testbench-20251113000943423.webp]]
4. Run the [[Vivado Behavioral Simulation]] simulation looks:
![[Testbench-20251113001046185.webp]]
