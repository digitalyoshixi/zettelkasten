---
tags:
  - java
aliases:
  - Java Input
  - Java User Input
---
This is a library used for getting user input.
# Usage
```java
import java.util.Scanner;
public class UserInput {
	Scanner input = new Scanner(System.in);
	int age;
	String name;
	System.out.print("What is your full name: ");
	name = input.nextLine(); // reads a string
	system.out.print("How old are you: ");
	age = input.nextInt(); // reads a integer
	input.close();
}
```
# Reading a number before a string
![[Pasted image 20230907193700.png]]
For some reason, nextInt() will not read in the escaped character newline. so, it leads to the next scan being a blank input.

The fix is to read as a string first, then convert it to number.
![[Pasted image 20230907194531.png]]
Consult [[Parsing]] For more details