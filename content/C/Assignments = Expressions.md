---
tags:
  - c
---
When you assign a value, you also return that value.

So, you can do things like this:

```c
int c;
while ((c = getchar()) != EOF){
	putchar(c);
}
```
c will get value from user value, then compare that given value with EOF.
*note that assignment matters a lot*
refer to [[Operator Precedence]]

It shortens code which would otherwise be like this:
```c
int c;
c = getchar();
while (c != EOF){
	c = getchar();
	putchar(c);
}
```