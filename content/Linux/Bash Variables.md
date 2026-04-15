---
tags:
  - bash
  - programming
aliases:
  - Bash Default Variables
  - Bash Special Variables
---
Creating a variable is done simply with: `variablename = value`
Calling a variable is done by preprending `$`. `echo $variablename`

```bash
#!/bin/bash
NAME=linux # remember NO SPACES
me="daniel" 
echo $NAME
echo ${NAME}taro #echo only given ammount
```
# Default Variables
```bash
FOO="${VARIABLE:-default}"  # FOO will be assigned 'default' value if VARIABLE not set or null.
```
# Special Variables
```bash
$0 # filename of current script
$n # n-th argument passed to script
$# # number of arguments passed to script
$@ # all arguments passed to script excluding $0
$* # all arguments passed to script
$? # exit status of program
$$ # PID of current shell
$! # process number of last background command
```