---
tags:
  - programming
---
A program that continues to output 'Give me a cookie' unless the user inputs 'cookie'
# Implementation
```c
#include <strings.h>
int main(){
	str userinput;
	while userinput != 'cookie'{
		printf("give me a cookie\n");
	}
	return 0;
}
```