---
tags:
  - programming
  - graphics
aliases:
  - OpenCL
  - OCL
---
A cross-platform graphics [[Application Program Interface|API]].
# [[Installable Client Driver|ICD]] Installation
```
yay -S ocl-icd opencl-headers clinfo 
```
### [[Shared Object]] Installation Nvidia GPU
```
yay -S opencl-nvidia
```
### [[Shared Object]] Installation AMD GPU
```
yay -S opencl-amd
```
# Concepts
- [[clinfo]]
- [[Installable Client Driver]]
- [[OpenCL Compute Host]]
- [[OpenCL Compute Unit]]
- [[Procesing Element|PE]]
- [[OpenCL Work Item]]
- [[OpenCL Work Group]]
- [[OpenCL Kernel]]
- [[OpenCL Loops to Kernels]]
- [[OpenCL Memory Model]]
- [[OpenCL Context]]
- [[Command Queue|OpenCL Command Queue]]
- [[OpenCL Program Object]]
- [[Buffer]]
- [[Image Object]]
- [[Opaque Data Structure]]
- [[Sampler]]
# Guides
- [[OpenCL Vector Addition Program]]
# Compilation Flag
```
gcc -Wall -Wextra -D CL_TARGET_OPENCL_VERSION=100 Main.c -o HelloOpenCL -lOpenCL
```
# Tutorials
- https://handsonopencl.github.io/
# References
- https://www.khronos.org/files/opencl-1-1-quick-reference-card.pdf