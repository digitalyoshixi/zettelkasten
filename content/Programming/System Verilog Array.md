---
tags:
  - verilog
  - programming
  - hardware
---
`<data_type>[data width]name_of_array;`
# Simple Declaration
```verilog
bit[8]array; // 8 element array
```
# Verbose Declaration
Alternate way to define the size of an array
```verilog
bit[7:0]array; // 8 element array
```
# Assignment
```verilog
array = `{2,4,12,1,4,6,2,3,9}; 
```
# Accessing Value
```verilog
array[0]; // will be 2
```
# 2D Array
```verilog
bit[2][3]array;
```