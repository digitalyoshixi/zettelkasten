---
tags:
  - programming
  - csharp
aliases:
  - C-Sharp Sealed Classes
  - C-Sharp Inheritence
---
# Normal Class
```cs
class MyClass {
	string myAttribute = "twilio";
	
	public MyClass(){
		// constructor logic
	}
	
	public void MyMethod(){
		Console.WriteLine(this.myAttribute);
	}
}
```
# Inheritence
```cs
class Car : Vehicle {
	// ...
}
```
# Sealed Classes
A class that cannot be inherited from
```cs
sealed class Infertile {
//...
}
```