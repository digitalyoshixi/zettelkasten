---
tags:
  - programming
  - c
---
Used for pattern matching strings.
- `%` can match zero or more characters
```c
%.txt : %.html
	lynx -dump $< > $@
```