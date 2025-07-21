---
tags:
  - programming
---
A [[Design Pattern]] for code structure.
Involves creating a facade class for clients, that abstracts the complexities of all the subsystem classes.
![[Facade Method-20250721135727262.webp]]
# Example
```java
public class Facade{
	Screen s;
	Light l;
	Projector p;
	public watchMovie(){
		s.on();
		l.dim()
		p.on();
	}
}

public class Client{
	Facade f;
	public void  watchMovie(){
		f.watchMovie();
	}	
}
```