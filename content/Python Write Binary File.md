---
tags:
  - python
aliases:
  - Python Create Binary File
---

```python
import struct
with open("my-file", "wb") as out_file:
  # this packs the integer 1337 (0x539 in hex) into four little-endian bytes
  out_file.write(struct.pack("<I", 1337))
  # the above is equivalent to
  out_file.write(b"\x39\x05\x00\x00")
  out_file.write(b"HELLO \"WORLD\"!")
  # this packs the integer 1337 (0x539 in hex) two little-endian bytes
  out_file.write(struct.pack("<H", 1337))
  # the above is equivalent to
  out_file.write(b"\x39\x05")
```