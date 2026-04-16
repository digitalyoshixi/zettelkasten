---
tags:
  - programming
  - os
aliases:
  - pthreads
---
The most common thread package on [[Unix]] systems.
# Process
1. Thread is created with [[pthread_create()]] to run a function, or to continue main
2. Thread terminates by returning from the given function or from main or from calling [[pthread_exit()]] 3. [[pthread_join()]] used to reap the return value from thread
# Functions
- [[pthread_create()]]
- [[pthread_join()]]
- [[pthread_exit()]]
- [[pthread_detach()]]
- [[pthread_self()]]
- [[pthread_mutex_init()]]
- [[pthread_mutex_lock()]]
- [[pthread_mutex_trylock()]]
- [[pthread_mutex_unlock()]]
- [[pthread_mutex_destroy()]]
# Examples
### Simple Fn Call Example
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <pthread.h>

typedef struct myArg {
	int fd;
	char name[25];
} MyArg;

void* myThreadLength(void *p){
	MyArg *theArg = (MyArg*)p;
	int* length = (int*)malloc(sizeof(int));
	*length = strlen(theArg->name);
	return length;
}

int main(){
	int fd = open("afile", O_RDWR);
	MyArg* p = (MyArg*)malloc(sizeof(MyArg));
	p->fd = fd;
	strncpy(p->name, "daniel", 7);
  p->name[6]='\0';

	pthread_t thread_ID;
	void* status;
	int err = pthread_create(&thread_ID, NULL, myThreadLength, (void*)p);
	if (err != 0) {
		printf("%s", strerror(err));
	}
  pthread_join(thread_ID, &status);
  printf("%d", *(int*)status);

  close(fd);
  return 0;
}
```
### Mutex Example
```c
pthread_mutex_t myMutex;
int status;

status = pthread_mutex_init(&myMutex, NULL);
if (status != 0) printf("%s", strerror(status));
pthread_mutex_lock(&myMutex);
// critical section here
pthread_mutex_unlock(&myMutex);

status = pthread_mutex_destroy(&myMutex);
if (status != 0) printf("%s", strerror(status));
```