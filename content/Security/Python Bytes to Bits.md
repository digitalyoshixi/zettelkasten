---
tags:
  - programming
  - python
aliases:
  - Python Bits to Bytes
---
# Bytes to Bits String
```python
def bytes_to_bitstring(b : bytes) -> str:
	return ''.join(f"{byte:08b}" for byte in b)
```
# Bits String to Bytes
```python
def bitstring_to_bytes(s : str) -> bytes:
    integer_value = int(s, 2)
    byte_length = (len(s) + 7) // 8
    return integer_value.to_bytes(byte_length, byteorder='big')

```