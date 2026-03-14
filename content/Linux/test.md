---
tags:
  - linux
---
A command used to return 0 or 1 as an [[Exit Codes]].
```bash
$ test 2 -lt 3
$ echo $?
0
$ test 3 -lt 3
$ echo $?
1
```