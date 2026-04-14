---
tags:
  - bash
  - programming
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