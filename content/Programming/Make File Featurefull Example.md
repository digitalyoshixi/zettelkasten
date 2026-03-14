---
tags:
  - programming
---
With the directory:
```
.
├── include
│   ├── y.c
│   └── z.h
├── lib
├── Makefile
└── x.c
```
# Makefile
```perl
CODEDIRS=. lib
INCDIRS=. ./include/
CC=gcc
OPT=-O0
CFLAGS=-Wall -Wextra -g $(foreach D,$(INCDIRS),-I($D)) $(OPT) $(DEPFLAGS)

CFILES=$(foreach D,$(CODEDIRS),$(wildcard $(D)/*.c))

all: $(BINARY)
$(BINARY): $(OBJECTS)
	$(CC) -o $@ $^
%.o:%.c

```