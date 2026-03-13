---
tags:
  - linux
---
A tool to view the decimal hexdump of a file.
# [[File Carving]]
```
dd if=<input_file> of=<output_file> bs=1 skip=<num_blocks> count=<num_count>
```
- `bs`: block size
- `skip`: number of blocks to skip
- `count`: number of blocks to copy