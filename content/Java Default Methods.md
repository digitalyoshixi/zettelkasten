---
tags:
  - programming
  - java
---
The ability to create default implementations of methods within a [[Java Interface]].
```java
public interface MyInterface {
	void show();
	default void myDefault(){
		// function body
	}
}
```