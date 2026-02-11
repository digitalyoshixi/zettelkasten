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
# Automatic Varialbes
- `$@` - the target filename
- `$*` - the target filename without file extension
- `$<` - first prerequisite filename
- `$^` - filename of all prerequisites sepereated by space
- `$+` - similar to `$^` but includes duplicates
- `$?` - names of all prerequisites 
# Environment Variable Check
Variables that will take on environment variables if they exist, if not then defaults to a default value.
```c
# if not defined in ENV variables, then take on default value '.'
GSL_INC ?= .
```