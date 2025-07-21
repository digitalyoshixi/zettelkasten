---
tags:
  - software
---
A design method that involves creating objects of unknown type, later resolved within the class.
![[Factory Method-20250721134911914.webp|439]]
Often done when you want to provide the option to instantiate two classes that are very similar.
# Example
```java
class Triangle extends Shape{
}
class Circle extends Shape{
}

abstract class GraphicsApplication{
	List<Shape> shapes;
	public abstract Shape factoryMethod();
	public void addShape(){
		Shape s = factoryMethod();
		shapes.add(s)
	}
}

public class CirclesApplications extends GraphicsApplication{
	public Shape createShape(){
		return new Circle();
	}
}

public class TrianglesApplicatiion extends GraphicsApplication{
	public Shape createShape(){
		return new Triangle();
	}
}

public class App{
	public static void main(String [] args){
		TrianglesApplication app = new TrianglesApplication();
		app.addShape();
	}
}
```