---
tags:
  - java
---
These are [[Java Class]] that cannot be directly [[Object|Instantiated]].
- Can have [[Abstract Methods]] and [[Concrete Methods]]
Commonly, you do not define any body for the abstract methods within the class.
# Boilerplate
```java
// Abstract class
abstract class Sunstar {
	private int a;
	public Sunstar(int a){
		this.a = a;
	}
    abstract void printInfo();
}

// Abstraction performed using extends
class Employee extends Sunstar {
    void printInfo()
    {
        String name = "avinash";
        int age = 21;
        float salary = 222.2F;

        System.out.println(name);
        System.out.println(age);
        System.out.println(salary);
    }
}
```