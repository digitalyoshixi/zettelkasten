---
tags:
  - java
---
# Opening A File
```java
import java.io.File;
import java.util.Scanner;
import java.io.IOException;
public class Main{
	public static void main (String[] args){
		File f = new File("./myfile.txt");
		System.out.println(f.isDirectory());
	}
}
```
# Reading File
![[Pasted image 20231115180010.png]]
