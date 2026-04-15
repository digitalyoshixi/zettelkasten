---
tags:
  - programming
  - c
aliases:
  - C pipe()
---
A [[Syscall]] used to create a [[Pipe]].
```c
int pipe(int pipefd[2]);
```
- Returns `0` on success
- Returns `-1` on error
```c
int fd[2]; // two arrays, fd[0] is read, fd[1] is write
pipe(fd);
```
![[Pipe-20260304010825785.webp|390]]
# Example Communication
```c
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

#define BUF_SIE 4 // small
#define MSG_SIZE 13 // small

int main(void){
	char *msg = "hello...world";
	char buf[BUF_SIZE];
	int p[2], nbytes;
	
	if (pipe(p) == -1){
		exit(1);
	}
	
	if (fork() == 0){ // child
		write(p[1], msg, MSG_SIZE);
		// close it
	} 
	else{ // parent
		close(p[1]);
		while ( (nbytes=read(p[0], buf, MSG_SIZE)) > 0){
			write(STDOUT_FILENO, bug, MSG_SIZE);
		}
	}
	return 0;
}
```
- If no writing end is open, the read detects an EOF and returns 0.