---
tags:
  - programming
---
A recursive function where the recursive call is the **last statement executed by a function**.
- Requires that there is some partial value to be called forward.

This is a more optimized way to write [[Recursion]], as the last statement of the final call will result in each subsequent stack frame being destroyed aswell.
# Example
### Non-Tail Function
```c
double sum_r(double *array, int n){
	if (n == 0){
		return *(array);
	}
	else{
		return ( *(array + n) + sum_r(array, n-1));
	}
}
```
### Tail Function
```c
double sum_tr(double *array, int n, double part_sum){
	if (n==0){
		return *(array);	
	}
	else{
		return sum_tr(array, n-1 , *(array+n));
	}
}
```