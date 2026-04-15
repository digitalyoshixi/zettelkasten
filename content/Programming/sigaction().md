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
- `signum` is the [[Signal]]'s number
- `act` is the sigaction struct
- `oldact` is the previous state of the signal
- Returns 0 on success
- Returns -1 on error
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
# Signal Masks
```c
int sigemptyset(sigset_t *set); // set mask no signal numbers
int sigfillset(sigset_t *set); // set mask all signal numbers
int sigaddset(sigset_t *set, int signo); // add signal to set
int sigdelset(sigset_t *set, int signo); // remove signal to set
int signalismember(sigset_t *set, int signo); // returns non-zero if signal part of set
```
- Used to store set of signals currently blocked
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
		if ((i++ % 50000000) == 0){
			fprintf(stderr,".");
		}
	}
	return 0;
}
```