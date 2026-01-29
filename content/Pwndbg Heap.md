---
tags:
  - debugging
  - memory
  - security
---
# Setting up Heap Variables
- You can see the heap variables with `heap-config`

- You can set `glibc` by using `info sharedlibrary`

- `heap` - displays state and address of heap chunks
- `bins/tcachebins/fastbins/smallbins/largebins` - displays state and chunks in each bin
- `vis-heap-chunks` - show hex dump of heap and marks chunks in bins