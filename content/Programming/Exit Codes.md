---
aliases: 
tags:
  - cpp
---
A number from $0-255$ representing the output status of a program.
Sent by the [[exit]] syscall.

Can be viewed with:
- [[WEXITSTATUS()]]
- [[WIFEXITED()]]
# Standard Meanings

| exit code | meaning                                                           |     |     |     |     |
| --------- | ----------------------------------------------------------------- | 
| 0         | everything is cool                                                |     |     |     |     |
| 1         | abnormal termination                                              |     |     |     |     |
| 2         | major abnormality(rare)                                           |     |     |     |     |
| 127       | command not found                                                 |     |     |     |     |
| 132       | SIGILL. aborted from illegal instruction                          |     |     |     |     |
| 133       | SIGTRAP. aborted from divide by zero                              |     |     |     |     |
| 134       | SIGABRT. aborted from failed assertation                          |     |     |     |     |
| 136       | SIGFPE. aborted from floating point exception or integer overflow |     |     |     |     |
| 137       | program took up too much memory                                   |     |     |     |     |
| 138       | SIGBUS. aborted from unaligned memory access                      |     |     |     |     |
| 139       | Segmentation fault. accessing memory not allocated to it          |     |     |     |     |
| 158/152   | SIGCPU. aborted through CPU time limit exceeded                   |         |     |     |
| 159/153   | SIGFSZ. aborted through file size limit exceeded                  |        |     |     |
