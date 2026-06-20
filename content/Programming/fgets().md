---
tags:
  - c
---
A function that gets the information from a file or input
```c
fgets(char *str, int STRLEN, FILE *stdin)
```
# Example
```c
int main(){
	char my_string[1024];
	fgets(mystring, 1024, stdin);
}
```