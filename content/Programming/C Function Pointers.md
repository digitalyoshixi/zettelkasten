---
tags:
  - c
  - programming
aliases:
  - FP
---
The addresses for each function in C can be passed as pointer to another function if required.
```c
void bye(){
	puts("goodbye");
}

void hello(void (*bye_func)() ){
	bye_func();
}

int main(){
	hello(bye);
}
```