---
tags:
  - c
  - programming
  - cpp
---
A buffer is a portion of memory that is constantly being read and written to.
This can be used for certain cases such as graphical buffers, input buffers, etc..
# Memory Allocation of a Buffer
The buffer is allocated on the heap.
1. The heap has more memory space
2. It can be freed whenever we need a new buffer
Buffers are saved as void ptrs. We just need the address, we dont care about the type of memory it is.
# Graphical Buffer
A graphical buffer will contain pixels which are 32bit structures. It will contain the # of pixels in the screen's resolution.
