---
tags:
  - programming
  - linux
---
A command used to create [[Pipe]] between processes.
```
mkfifo ./pipefile
```
# Usage
```bash
echo hi > pipe # process 1
cat pipe # process 2
```