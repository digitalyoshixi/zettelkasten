---
tags:
  - programming
  - software
---
A [[Design Pattern]] that involves creating frequently modifiable classes.
![[Strategy Method-20250721144055492.webp]]
# Example
```java

public interface DateFormatStrategy{
	public String format(int day, int month, int year);
}

class DMYStrategy implements DateFormatStrategy{
	public String format(int day, int month, int year){
		return day + "/" + month + "/" + year;
	}
}
class MDYStrategy implements DateFormatStrategy{
	public String format(int day, int month, int year){
		return month + "/" + day + "/" + year;
	}
}

public class Main{
	public static void main(String [] args){
		Date d  = new Date(21, 7, 2025);
		d.setStrategy(new DMYStrategy());
		System.out.println(d); // will print 21/7/2025
	}
}
```