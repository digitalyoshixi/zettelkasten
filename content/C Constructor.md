---
tags:
  - programming
  - c
---
These are functions that run before the program launches
```
__attribute__((constructor)) void haha()
{
	puts("hello world!");
}
```
