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
	$(CC) $(CCFLAGS) $(LDFLAGS) $@ $^
	
.PHONY: clean // not a file, but a command
clean:
	rm -f hellow *.o

%.o: %.c sorts.h
	gcc -c $< -o $@
// wildcard .o, wildcard .c, $@ name of target, $<, name of first argument
```
Has commands:
- `make all`
- `make hellow`
- `make clean`
# Usage
```
make
```
- Runs the first rule it finds
```
make rule
```
- Runs the given rule
```
make -j 8
```
- Run 8 jobs to execute recipes simultaneously
```
make help
```
- Returns the self-written [[Make Comments]]
# Concepts
- [[Make Variable]]
- [[Make Rules]]
- [[Make Suffix Rules]]
- [[Make Pattern Rules]]
- [[Make Target]]
- [[Make Command]]
- [[Make Invisible Command]]
- [[Make PHONY Target]]
- [[Make Dependency Graph]]
- [[Make Comments]]
# Examples
- [[Make File Featurefull Example]]