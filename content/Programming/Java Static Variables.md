---
tags:
  - programming
---
Static makes everything shared.

essentially the metadata of your class.
# Static Variables
its a variable or method shared across all classes. Changing this static variable will change the static variable in all other objects
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
