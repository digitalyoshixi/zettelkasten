---
tags:
  - programming
---
A dummy implementation of a method and expected method return.

Allows mock objects to have methods that return values (though not necessarily correct).

[[Mockito When]] and [[Mockito ThenReturn]] can simulate stubs without need to create new classes.
# Example
```java
public interface TodoService{
	public List<String> retrieveTodos(String user);
}
public class TodoServiceStub implements TodoService{
	public List<String> retrieveTodos(String user){
		return Arrays.asList("Learn jenkin", "Learn spring");
	}
}
```