---
tags:
  - programming
---
An [[Object Oriented Programming|OOP]] [[Design Pattern]] that separates algorithm from object structure.
A visitor is an object with methods for acting on various kinds of other objects.
![[Visitor Pattern-20250701160154285.webp]]
- Allows adding more functionality to a class without modifying its structure, thereby allowing inheriting classes to remain the same
# Example
```cpp
class BinaryOperation : public Expression {
	// call a visitor method named visit that takes this current binary operator as the argument
	v.visit(*this);
}
```
```cpp
class PrintingVisitor : public Visitor {
	void visit(BinaryOperator &o){
		std::cout << '('; // print opening parenthesis
		o.left.accept(*this); // print left operand
		std::cout << o.op; // print operator
		o.right.accept(*this); // print right operand
		std::cout << ')'; // print closing parenthesis
	}
}
```