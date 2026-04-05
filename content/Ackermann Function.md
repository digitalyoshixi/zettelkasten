---
tags:
  - programming
---
A [[Recursion|Recursive Function]] that can only be implemented recursively. There is no iterative variant.
# Function
With $m,n \geq 0$:
```cpp
#include <stdio.h>

int ack(int m, int n){
	int asn;
	if (m == 0) ans = n+1;
	else if (n == 0) ans = ack(m-1, 1);
	else ans = ack(m-1, ack(m,n-1));
	return ans;
}
```