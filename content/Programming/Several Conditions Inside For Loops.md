---
tags:
  - c
---
for loops generally look like: `for (counter initialization; condition; do after every iteration)`
the condition part is usually something like `i<10`
But, you can also make it a combined boolean too.

For example:
```c
int c,i;
for (i = 0; i < 10 && ((c = getchar()) != EOF) && c != '\n'; i++){
	printf("%c",c);
}
```
the condition is a combined boolean