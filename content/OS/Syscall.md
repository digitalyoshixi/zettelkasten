---
tags:
  - os
  - syscall
aliases:
  - Syscalls
  - System Calls
---
## System calls:
Provide an interface to the services made by an OS. 
There are 2 modes of execution: User and Kernel mode [[Permissions]] Think of it as running as an administrator.
### Usermode
The processor can access only a limited amount of resources and instructions. This can be memory, I/O devices and CPU registers.
### Kernelmode
Privileged mode where the kernel operates. Access to all system resources. Can perform low-level operations and interact with hardware directly
### System call
Are calls made by a program to the OS in order to access resources not accessible through usermode.It is a special call made by switching from user mode to kernel mode. This process is called mode-shifting. The process is as follows:

1. User made program calls a system call. Usually through a library function or interrupt.
    
2. Processor switches from usermode to kernelmode. Save the current state of user program’s register values, program counter onto the kernel stack
    
3. Os identifies the operation and executes. May allocate, delete, modify resources or perform I/O operations
    
4. Saves results of operation to the stack and switches back to user mode
    
  
### Types of System calls

1. Process control
- End/abort
- Load/execute
- Create
- Terminate
- Get process attributes
- Wait
- Wait for event/Fire event
- Allocate and free memory
    

2. File manipulation
- Create a file
- Delete a file
- Open
- Close
- Read
- Write
- Change directory
- Get attributes and set attributes
    

3. Device management
- Request device
- Release device
- Read, write, change directory
- Get attributes and set attributes
- Attach or detach devices
    

4. Information maintenance
- Get/Set time, date
- Get/Set system data
- Get/set process, file or device attribute
    

5. Communications
- Create or delete processor connections
- Send/Receive messages
- Transfer status information. Get current progressive from a process
- Attach or detach remote devices
    