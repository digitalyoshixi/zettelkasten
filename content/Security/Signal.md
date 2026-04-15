---
tags:
  - linux
  - os
aliases:
---
Communication signals sent from the OS to a process.
Whenever these signals are sent to the process, the program must halt and handle this signal with its custom-defined handler function

# Signal Representation
OS uses a [[Bitmap]] to represent signals pending and blocked
![[Signal-20260415202520823.webp]]
- Pending signals will be processed by the [[sigaction()|Signal Handler]]
- Blocked signals when found will cause the process to restart
# Signal List
https://www.computerhope.com/unix/signals.htm
- [[SIGHUP]]
- [[SIGINT]]
- [[SIGQUIT]]
- [[SIGILL]]
- [[SIGTRAP]]
- [[SIGABRT]]
- [[SIGEMT]]
- [[SIGFPE]]
- [[SIGKILL]]
- [[SIGBUS]]
- [[SIGSEGV]]
- [[SIGSYS]]
- [[SIGPIPE]]
- [[SIGALRM]]
- [[SIGTERM]]
- [[SIGURG]]
- [[SIGSTOP]]
- [[SIGTSTP]]
- [[SIGCONT]]
- [[SIGCHLD]]