---
tags:
  - linux
---
A method used to establish [[Interprocess Communication|IPC]] between processes of the parent and child.
- [[Child Process]] shares the same pipes to allow for child-parent communication
- Pipes are unidirectional, you can read and write from same ppe
   ![[Pipe-20260304011051194.webp]]
# Reading Writing Pipe
- The writing pipe will write only if the reading pipe is empty or null
- The reading pipe can read only if the writing pipe is empty or null
# Pipe Communication Types
### Self Communication
1. Create a pipe
2. Send a message to the pipe
3. Retrieve message from pipe, write it to [[Standard Output|stdout]]
4. Send another message to pipe
5. Retrieve message from pipe and write to [[Standard Output|stdout]]
### Parent Child Communication
1. Create a pipe
2. Create a child process
3. Parent process writes to pipe
4. Child process retrieves message from pipe and writes to [[Standard Output|stdout]]
### Two-way Communication
1. Create two pipes:
	1. Pipe1: parent to write and child to read
	2. Pip2: child to write and parent to read
2. Create child process
3. Close unwanted ends not needed for process communication
4. Close unwanted ends in parent process: read end of pipe1, write end of pipe2
5. Close unwanted ends in child process: write end of pipe1, read end of pipe2
6. Perform communication as required
# Syscalls
- [[pipe()]]