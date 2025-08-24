---
tags:
  - malware
  - cryptography
aliases:
  - UPX
---
UPX is a very simple packing tool for windows and linux systems.
Uses the [[UCL]] [[Compression Algorithm]] to pack, and runs the decompressor on program start.
# Unpacking
Get the UPX tool.
`sudo pacman -S upx`
and then run
`upx -d filename`
to unpack a file.
Let [[Ghidra]] do the heavy lifting afterwards