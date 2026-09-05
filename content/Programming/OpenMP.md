---
tags:
  - programming
  - os
aliases:
  - OMP
---
Uses explicit [[Parallelism]] with [[OpenMP Fork Join Model]]
![[OpenMP-20260416001705494.webp]]
# Example
```c
#include <omp.h>

main(){
	int nthreads, tid;
	#pragma omp parallel private(tid) {
		tid = omp_get_thread_num();
		printf("%d", tid);
		
		if (tid == 0) {
			nthreads = omp_get_num_threads();
			printf("num threads %d\n", nthreads)
		}
	}
}
```