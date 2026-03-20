---
tags:
  - java
  - programming
aliases:
  - Java implements
  - Java Implementation
---
These are [[Interface|Interfaces]] defined for [[Java]].
They act like public facing APIs.
They are similar to [[Java Abstract Class]], but they:
- Cannot have any [[Concrete Methods]]
- Can have [[Java Default Methods]]
- The only attributes allowed must be `final static` attributes (attributes are not well supported)
# Implementing a Interface
```java
class myClass implements myInterface{
	// ...
}
```
# Boilerplate
```java
interface Animal {
  public static int mytag;
  public void animalSound(); // interface method (does not have a body)
  public void run(); // interface method (does not have a body)
  
  public default void die(){
	  System.out.println("poof");
  }
}
```
