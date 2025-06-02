---
tags:
  - java
---
These are [[Java Classes]] that cannot be directly [[Object|Instantiated]].
Used to make [[Abstraction]] easier.
Commonly, you do not define any body for the abstract methods within the class.
# Boilerplate
```java
// Abstract class
abstract class Sunstar {
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