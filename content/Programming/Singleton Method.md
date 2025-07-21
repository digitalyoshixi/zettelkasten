---
tags:
  - software
---
Used to ensure that a class only has one instance, and provide a global point of access to it. 
Often used when you only want one session. For:
- Database communication
# Implementation
- You have to make the object static
- You will have a private constructor method for creating the instance
- You need to have a condition in the constructor that checks if there already exists a singleton, if not, then it will construct using the private constructor method.

```java
// final class to prevent other classes from extending it
final class Manager {
	private static Manager manager;
	private Manager() {
	}
	public static Manager getInstnace(){
		if (manager == null){
			manager = new Manager();
		}
		return manager;
	}
}
```