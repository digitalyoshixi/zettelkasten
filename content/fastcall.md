---
tags:
  - security
  - linux
aliases:
---
# Process
1. First two arguments are saved into arg2: `rbx`, arg1: `rcx`
2. Function is called with `call <location>` & `rip` pushed
3. Space is allocated onto the stack for local variables
4. Function does work
5. Stack is restored
6. Returns by calling `ret`
7. Stack adjusted to remove arguments
# Example
With C code:
```c
__attribute__((fastcall)) void printnums(int num1, int num2, int num3){
	printf("The numbers you sent are: %d %d %d", num1, num2, num3);
}

int main(){
	printnums(1, 2, 3);
	return 0;
}
```
