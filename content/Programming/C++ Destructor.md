---
tags:
  - cpp
  - programming
aliases:
  - C++ Default Destructor
---
This is a destructor method for [[C++ Class]]
```cpp
class MyClass
{
	~MyClass() {
		printf("destructor called!");
	}
}
```
# Default Destructor
Deletes the allocated heap memory of a class.
Does not remove:
- Additional [[C malloc]]'d memory
- Pointers to the class
```cpp

```