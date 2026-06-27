---
tags:
  - programming
---
Objects are created when you instantiate a [[Java Class]]
Objects are [[Pass by Reference]].
# Instantiation
```java
//defined class myObject
public class myObject {
  int x = 5;
}
public class Main{
  public static void main(String[] args) {
	// instantiation
    Main myObj = new myObject();
    System.out.println(myObj.x);
  }
}

```
# Methods
- [[Java .equals()]]
- [[Java .hashCode()]]
- [[Java .toString()]]