---
tags:
  - linux
---
A method used to establish [[Interprocess Communication|IPC]] between processes of the parent and child.
1. Children share the same pipe. Allows for child-parent process communication
   ![[Pipe-20260304011051194.webp]]
2. Pipes are unidirectional. You can read and write from the same pipe