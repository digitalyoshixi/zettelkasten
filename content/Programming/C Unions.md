---
tags:
  - c
---
Unions are like [[C Structures|Struct]], but they allow several datatypes to use the same memory location.
- Changing the value of one member will change the value of all other members

```c
union union_tag{
	datatype1 attr1;
	datatype2 attr2;

} some_union_vars...;
```

# Dynamic Size
https://www.youtube.com/watch?v=ZMzdrEYKyFQ
Usually when structures are declared, the sum of all of the size of its attributes is allocated to the stack/heap.
Unions will only allocate the **largest** attribute. all attributes will then share this allocated memory space.

### Polymorphism
Because all elements share the same memory, if you wanted to use a datatype as another datatype, that is possible too
```c
#include <stdio.h>
#include <string.h>

union myunion{
	int layers;
	char type[20];
};
int main(){
	union myunion = {5};
	strcpy(myunion, "green");
	printf("%d", myunion.type); // string as int. will be 0000
	return 0;
}
```
