---
tags:
  - programming
---
A program is linearly recursive if there is at most one recursive call made in any execution/path of function body.
# Examples
```c
int myfunc(int a){
	if (a < 0) return a;
	return myfunc(a-1);
}
```

```c
int myfunc(int a){
	if (a < 0) return a;
	if (a % 2 == 0){
		return myfunc(a-1);
	}
	else{
		return myfunc(a-2);
	}
}
```