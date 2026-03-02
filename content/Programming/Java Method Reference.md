---
tags:
  - programming
  - java
---
A shorthand way to refer to a method in java without invoking them.
Used as an alternative to [[Java Lambda Function]].
Uses `::` operator.
# Example
```java
import java.util.Arrays;
public class MyClass{
	
	public static void print(String s){
		System.out.println(s);
	}
	
	public static void main(String[] args){
		String[] names = {"thing1", "thing2", "thing3"};
		Arrays.stream(names).forEach(MyClass::print); // using method refs
	}
}

```