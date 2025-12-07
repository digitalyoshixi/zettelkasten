---
tags:
  - linux
  - programming
---
A tool used to assist in compiling and lining [[C]] code.
# Example
```c
all: hellow
hellow: hellow.c
	gcc -o hellow hellow.c
clean:
	rm -f hellow
```
Has commands:
- `make all`
- `make hellow`
- `make clean`
