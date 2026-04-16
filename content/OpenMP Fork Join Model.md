---
tags:
  - programming
  - c
---
```c
#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include <omp.h>

int main(){
	// fork()
	#pragma omp parallel for
	for (int i=1; i < 10; i++){
		printf("hello from %d thread %d\n", i, omp_get_thread_num());
	}
	return 0;
}
```