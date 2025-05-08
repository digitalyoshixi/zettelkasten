---
tags:
  - verilog
  - programming
  - hardware
---
`<data_type> <array_name> [];`
# Example
```verilog
bit[7:0]d_array1[]; // [] to signal dynamic array
d_array1 = new[4]; // make a dynamic array of 6 elements
d_array1 = `{1,2,3,4,5,6};
d_array1 = new[10]; // given 10 new memory locations, all old values deleted
d_array1 = new[10](d_array1) // given new memory location with all old values kept!
```