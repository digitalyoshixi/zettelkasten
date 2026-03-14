---
tags:
  - programming
---
[[Java|Javas]] implementation of [[Generics]]
This is a way to parameterize types.

```java
public class Pair<E> {
	E o1;
	E o2;
}
```
# Type Restrictions
```java
public class Pair<E extends T>{
	// ...
}
```