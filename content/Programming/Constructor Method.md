---
tags:
  - programming
---
The constructor method is ran at the start of instantiation

# 2 Constructor Tricks
'this' allows us to be self referential
```java
// no argument constructor
public Fraction(){
	this(1,1) // calling the other Fraction() method
}
// argument constructor
public Fraction(int num, int den){
	this.num = num;
	this.den = den;
}
```
