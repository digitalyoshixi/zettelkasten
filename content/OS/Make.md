---
tags:
  - linux
  - programming
aliases:
  - Makefile
---
A tool used to assist in compiling and lining [[C]] code.
makefiles are defined in:
- `makefile`
- `Makefile`
- `GNUmakefile`
# Example
```c
CC = gcc

CCFLAGS = -I$(GSL_INC) -O2
LDFLAGS = -L$(GSL_LIB)

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
# Concepts
- [[Make Variable]]
- [[Make Suffix Rules]]
- [[Make Pattern Rules]]
- [[Make Target]]
- [[Make PHONY Target]]
- [[Make Dependency Graph]]