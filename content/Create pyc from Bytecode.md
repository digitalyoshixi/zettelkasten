---
tags:
  - programming
  - python
---
```python
import struct
import time
import importlib

code = compile("print('hello')", "example.py", "exec")
[magic_number] = struct.unpack("<H", importlib.util.MAGIC_NUMBER[:-2])
pyc_content = struct.pack('<I', magic_number) # Magic number
pyc_content += struct.pack('<I', 0) # Flags
pyc_content += struct.pack('<I', int(time.time())) # Timestamp
pyc_content += marshal.dumps(sequencer_code) # Marshalled code object
# Write to file
with open('example.pyc', 'wb') as f:
	f.write(pyc_content)
```