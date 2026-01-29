---
tags:
  - security
  - c
aliases:
  - UAF
---
A common vulnerability in memory-unsafe programs.
Occurs when the program attempts to access memory already freed.
Can lead to future exploitation, [[Memory Disclosure]] or [[Metadata Corruption]]
# Example
```
int main(){
	char *user_input = malloc(8);
	scanf("%7s", user_input);
	free(user_input);
	long *authenticated = malloc(8);
	*authenticated = 0;
	scanf("%7s", user_input);
	
	if(*authenticated) printf("WIN!");
}
```