---
tags:
  - programming
  - c
---
A [[Make Target]] that does not have any dependencies.
Often used for:
- Cleanup
- Variables
```c
.PHONY: variables
variables:
	@echo TXT_FILES: $(TXT_FILES)
```

```c
.PHONY: clean
clean:
	rm -f *.dat
	rm -f results.txt
```