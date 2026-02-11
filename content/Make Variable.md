---
tags:
  - programming
  - c
---
A usage of macros and variables.
```c
PACKAGE = gnunode
VERSION = ` date+%Y.%m.%d `
ARCHIVE + $(PACKAGE)-$(VERSION)

dist:
	tar -cf $(ARCHIVE).tar .
```