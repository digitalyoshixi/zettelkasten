---
tags:
  - programming
aliases:
  - Early Exit
---
`continue` skip the current code block and go to next iteration of loop.
Opposite of [[Break]].
# Example
```java
while (true){
	if (x % 2 == 0){
		continue;
	}
	x--;
}
```