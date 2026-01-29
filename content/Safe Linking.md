---
tags:
  - security
  - memory
  - programming
---
Malloc attempts to encrypt single-linked list pointers by taking the position of where ptr is stored and encrypting it with ASLR bits of the position.
```
(pos >> 12) ^ ptr
```
# Bypassing
- If position and ptr and in the same page, then you can get the heap base:
```python
def deobfuscate(val):
	mask = 0xfff << 52
	while mask:
		v = val & mask
		val ^= (v >> 12)
		mask >>= 12
	return val
```