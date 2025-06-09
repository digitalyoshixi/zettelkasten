---
tags:
  - java
---
This is a library that implements [[Generics]] as an [[Linked List|List]]
# Example
```java
import java.util.ArrayList

public class Driver {
	public static void main(String[] args){
		ArrayList<String> mylist = new ArrayList<String>();
		mylist.add("abc"); // adding "abc"
		System.out.println(mylist.contains("abc")); //true
	}
}
```
# Methods
### .contains()
This will use the datatypes, [[Java .equals()]] method to check, so make sure to overwrite this for custom classes.