---
tags:
  - c
aliases:
  - Macro Substitution
  - C Constants
---
A type of [[Preprocessor Directives]] used to make constants.
They can only be one line long and cannot use `;`
# Constants
A way to avoid [[Magic Numbers]]
```c
#define LOWER 10

int main(){
	printf("%d", 7+LOWER);
}
```
# Mini Lambdas
```
#define max(A, B) ((A) > (B) ? (A) : (B))
```
Uses the [[Conditional Operator|Ternary Operator]]
