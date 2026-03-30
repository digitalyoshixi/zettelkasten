---
tags:
  - programming
---
A [[Data Structures and Algorithms|Data Structure]] used for storing memory.
- Very fast
- Cannot free added data, must clear the entire arena
```c
struct arena {
	uint8_t *offset;
	void *data;
	size_t capacity;
}
```