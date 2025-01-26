---
tags:
  - OOP
---
```java
public class Fraction{
	private int num; // IMPORTANT!! PRIVATE
	private int den; // IMPORTANT!! PRIVATE

	// Accessors
	public int getNum(){
		return num;
	}
	public int getDen(){
		return den;
	}
	// Mutators
	public void setNum(int newnum){
		this.num = newnum;
	}
	public void setDen(int newden){
		if (newden!=0){
			this.den = 1;
		}
		else{
			this.den = newden;
		}
	}

}
```