---
tags:
  - binary_exploitation
  - security
---
```python
p32(0x08048087)
esp = unpack(p.read()[:4])
print(hex(esp))
```