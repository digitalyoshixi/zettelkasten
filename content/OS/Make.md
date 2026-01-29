---
tags:
  - linux
  - programming
---
A tool used to assist in compiling and lining [[C]] code.
makefiles are defined in `./makefile`
# Example
```c
all: hellow
hellow: hellow.c
	gcc -o hellow hellow.c
	
.PHONY: clean // not a file, but a command
clean:
	rm -f hellow

%.o: %.c sorts.h
	gcc -c $< -o $@
// wildcard .o, wildcard .c, $@ name of target, $<, name of first argument
```
Has commands:
- `make all`
- `make hellow`
- `make clean`