---
tags:
  - programming
  - graphics
---
A object representing a given program. Contains:
- [[OpenCL Context]]
- [[OpenCL Kernel]] source or binary
- List of target devices
Can compile into [[Graphics Card|GPU]] or [[Central Processing Unit|CPU]] code.
# Creation
- `cICreateProgramWithSource()`
- `cICreateProgramWithBinary()`