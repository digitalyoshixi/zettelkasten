---
tags:
  - c
---
Defining [[C Structures]] as types. Evaluated at compile-time

```c
typedef unsigned int size_t;
typedef unsigned int age_t;
typedef unsigned int shoe_size_t;
```

```c
typedef struct some_struct
{
	// entries in the struct
} datatypename;
```
# TypeDef [[C Function Pointers]]
```c
typedef return_type (*alias_name)(parameter_types and numbers....);
```
# Example
```c
typedef struct Node {
	int x;
	struct Node *next;
}Node;
```