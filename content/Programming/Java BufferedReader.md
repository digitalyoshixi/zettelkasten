---
tags:
  - java
  - programming
---
Java library to read files in a format. Character by character, or word by word.
# Reading File Line-by-line
```java
BufferedReader input = new BufferedReader(new FileReader(""));
Stirng line = input.readLine();
while(line != null){
	System.out.println(line);
	line = input.readLine();
}
```