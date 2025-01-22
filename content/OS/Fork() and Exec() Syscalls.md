---
tags:
  - os
  - syscall
---
Fork() is a system call to create duplicate processes

A fork in c code runs the code again. The code runs exponentially from each fork. Let p represent # of times program runs, f represent # of forks. p(f) = 2^f. So 3 forks will result in 8 program runs.

Exec() run a new process over the only one. The new process will have the same process ID as the old one, but yes you can run another program and once that program finishes, it returns to the parent program

  

Multiple threads may work on the same task. If one thread completes the task, then all other ‘target threads’ will be canceled.

Async cancellation: thread that won tells other threads to terminate

Deferred cancellation: target thread periodically checks if it should terminate

### Threading issues
 
|Issue|Solution|
|------|---------|
|If a thread calls fork(), do we duplicate all other threads?|There are 2 versions of fork()<br><br>1. duplicate all threads<br>    <br>2. Only duplicate the thread that invoked fork().<br>    <br><br>If exec() is called after forking, then only duplicate one thread. it would be useless to duplicate all threads because they will all be replaced with exec()<br><br>Else, we should duplicate all threads. 2^f exponentials!!!|
|If a target thread is canceled while updating data, what happens?|Async: Os will reclaim system resources from a canceled thread, but not all<br><br>Deferred: Os reclaims all the data|