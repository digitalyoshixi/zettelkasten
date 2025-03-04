---
tags:
  - programming
---
A class is essentially a blueprint for you to

To make a class do this:
```java
public class Car{
	private String color;
	private String make;
	private String model;
	private String engineType;
	// constructor
	public Car(String color, String make, String model, String engineType){
		// adjust attributes
		this.color = color;
		this.make = make;
		this.model = model;
		this.engineType =  engineType;
	}
	// methods
	public void setColor(String color){
		this.color = color;
	} 
	


}

```