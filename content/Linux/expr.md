---
tags:
  - linux
---
A [[POSIX]] command to execute an expression and perform [[Command Line Substitution|CLS]]
```sh
expr 4 + 1
expr 4 \* 2
expr 4 / 2
expr 4 \> 2
expr 4 \< 2
```

```shell
i = `expr $i + 1`
```