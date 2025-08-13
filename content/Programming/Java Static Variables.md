---
tags:
  - programming
---
Variables/methods that are loaded once per class (not instance).
- Each variable or method is shared between all objects
Used mainly for utility variables/operations.
They can be directly invoked from the class name itself.
# Static Variables
Its a variable or method shared across all classes.
Changing this static variable will change the static variable in all other objects
# Static Methods 
will run from the variables in the class itself instead of the current object
### Example
```java
public class Fraction{
	private int num;
	private int den;
    private final int DEFAULT_DENOMINATOR = 1;
	private static int numberOfFractions = 0; // our static variable

	public Fraction() {
	     numberOfFractions++;
	}

    public static int getNumberOfFractions() { // static methods. will not get from this object. will get it from the entire class
        return numberOfFractions;
    }
}
```
### Requirements:
- Static variables used can only be use in static methods.
- returning static variables must not have a `this.` before it
- static variables should be private is possible
