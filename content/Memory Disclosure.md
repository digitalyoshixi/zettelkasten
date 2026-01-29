---
tags:
  - security
  - binary_exploitation
---
Unauthorized access and exposure of sensitive data in memory.
Can often be caused by [[Use After Free|UAF]].
# UAF Example
```c
int main(){
	char *name = malloc(8);
	
	printf("Name? ");
	scanf("%7s", name);
	printf("Hello %s!\n", name);
	free(name);
	
	printf("Goodbye, %s!\n", name);
}
```