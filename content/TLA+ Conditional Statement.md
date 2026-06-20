---
tags:
  - programming
  - verification
---
```tla
IF pc = "start"
	THEN expr1
	ELSE expr2
```
# Nested Conditionals
```tla
IF cond
	THEN expr1
	ELSE IF cond
		THEN expr2
		ELSE expr3
```