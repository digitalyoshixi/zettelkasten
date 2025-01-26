---
tags:
  - python
---
`round(number, ndigits)`
Where:
- `float number` is the number we want to round
- `int ndigits` is the offset from the decimal place
# Rounding Logic
- If number ends at 0.5, it rounds to the **nearest even number**.
  example:
	- round(0.5) = 0
	- round(1.5) = 2
- If `ndigits` < 0, then we are going to round in the 1s, 10s, 100s, etc.
  example:
	- round(256.56, -2) = 300
- If ndigits = 0, or it is omited, then it returns an `int`
# Return
Can return float if ndigits $> 1$ or int if ndigits is not provided