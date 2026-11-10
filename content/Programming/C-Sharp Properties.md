---
tags:
  - programming
  - csharp
---
```cs
class Person
{
	public string Name { 
		get {return name;}
		set {name = value;}
		}
}
```
- Automatically creates a `.get()` method
- Automatically creates a `.set(value)` method
# Automatic Logic
```cs
class Person
{
	public string name {get; set;}
}
```
- Default `.get()` is `return name;`
- Default `.set(value)` is `name = value`