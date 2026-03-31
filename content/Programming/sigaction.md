---
tags:
  - programming
aliases:
  - C Signal Handling
---
A [[C]] function that is used to overwrite the [[Process Control Block|PCB]] signal table so that once a signal is recieved, it will call a given function.
```c
int sigaction(int signum, const struct sigaction *act, struct sigaction *oldact)
```
- `signum` is the [[Signal]]'s number\
- `act` is the sigaction struct
- `oldact` is the previous state of the signal
# Sigaction struct
```c
struct sigaction{
	void (*sa_handler)(int);
	void (*a_sigaction)(int, siginfo_y*, void*);
	sigset_t sa_mask;
	int sa_flags;
	void (*sa_restorer)(void);
}
```
# Example
```c
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>

void handler(int code){
	fprintf(stderr, "Signal %d caught\n", code);
}
int main(){
	int i = 0;
	struct sigaction newact;
	newact.sa_handler = handler;
	newact.sa_flags = 0; // default flags
	sigemptyset(&newact.sa_mask) ; // block no signals during handler
	sigaction(SIGINT, &newact, NULL);
	
	for (;;){
		if ((1++ % 50000000) == 0){
			fprintf("stderr",".");
		}
	}
	return 0;
}
```