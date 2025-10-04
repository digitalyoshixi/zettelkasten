---
tags:
  - math
aliases:
  - GCD
  - Euclid's Algorithm to find GCD
---
The largest divisor that is shared between two numbers.
# Euclid's Algorithm to find GCD
```python
while a != b:
	if a > b:
		a = a - b
	else:
		b = b - a
```
At the end, `a` will store the common divisor between original `a` and `b`