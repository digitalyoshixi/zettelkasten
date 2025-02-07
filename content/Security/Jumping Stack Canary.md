---
tags:
  - security
  - binary_exploitation
---
If the situation allows for it, you can overwrite the read point of the program to skip past the stack canary.

```c
int main(){
	char buf[16];
	int i;
	for (i = 0; i < 128; i++){
		read(0, buf+i, 1);
	}
}
```