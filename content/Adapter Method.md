---
tags:
  - programming
---
A [[Design Pattern]] centered around adapting classes to specific [[Interface|Interfaces]].
![[Adapter Method-20250721144118170.webp]]
# Implementation

```java
interface Target{
	public int add(int a, int b);
}

class Adaptee(){
	public int sum(a,b){
		return a + b;
	}
}

class Adapter implements Target{
	Adapter(){
	}
	public int add(int a, int b){
		return adaptee.sum(a,b);
	}
}

```