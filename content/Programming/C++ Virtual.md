---
tags:
  - c
  - programming
---
This keyword allows a child class to override the function.
# Not Implemented Virtual Function
A not implemented function will equal `= 0`. Its a syntax quirk of [[C++]]
```cpp
class ExprAST{
public:
	virtual ~ExprAST() {}
	virtual Value *codegen() = 0; // = 0 means not implemented
}
```