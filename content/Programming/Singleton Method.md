---
tags:
  - software
---
Used to ensure that a class only has one instance, and provide a global point of access to it. 
![[Singleton Method-20250721144322596.webp]]
Often used when you only want one session. For:
- Database communication
# Implementation
```java
// final class to prevent other classes from extending it
final class Manager {
	private static Manager manager;
	private Manager() {
	}
	public static Manager getInstance(){
		if (manager == null){
			manager = new Manager();
		}
		return manager;
	}
}
```