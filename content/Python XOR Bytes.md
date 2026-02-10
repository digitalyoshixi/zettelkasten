---
tags:
  - programming
  - python
  - cryptography
---
```python
one = bytes.fromhex("0bfd0bc8fce6203048d261ee123e4d20a976e855da6cb1dd4b43226a2b0b2b6fd5c22d1dbb24e54cecabc443c33437ad7d7061a39523127f1813")
two = bytes.fromhex("7b8a65e69f894c5c2db504955b7c397aeb1bd02c9808d7940f6e11066c465d3685885942e14cd16288f9be0db97973e14d310beeef7268286519")

one_xor_two = bytes(a ^ b for (a, b) in zip(one, two))
```