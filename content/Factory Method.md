---
tags:
  - software
---
A design method that involves creating objects of unknown type, later resolved within the class.
Often done when you want to provide the option to instantiate two classes that are very similar.
# Example
```java
class Triangle extends Shape{
}

abstract class GraphicsApplication{
	List<Shape> shapes;
	public abstract Shape factoryMethod();
	public void addShape(){
		Shape s = factoryMethod();
		shapes.add(s)
	}
}
```