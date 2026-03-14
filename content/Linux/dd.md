---
tags:
  - linux
aliases:
  - DD Image
---
A tool used to convert and copy a file
# Imaging
Creating a [[Forensic Copy]] of a file.
# [[File Carving]]
```
dd if=<input_file> of=<output_file> bs=1 skip=<num_blocks> count=<num_count>
```
- `bs`: block size
- `skip`: number of blocks to skip
- `count`: number of blocks to copy