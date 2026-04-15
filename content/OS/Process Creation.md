---
tags:
  - os
---
The method to create a process
# Process
1. [[fork()|fork]] to make a child, child makes new [[Process Control Block|PCB]]
2. [[execve]] to replace child with new program
Can optionally share data with parent via [[Pipe]]