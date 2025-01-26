---
tags:
  - c
---
All labels are local.

These are pieces of your code, they are NOT functions. 
They do not take arguments or anything. 
They are literally blocks in your code that you can jump to and continue execution from.

For example:
```c
int main(){
	goto stuff1;
	stuff1:
		printf("hi");
		goto stuff2;
	stuff2:
		printf("hello");
		goto stuff3;
	stuff3:
		return 0;
}
```
output is: `hihello`
and then program ends