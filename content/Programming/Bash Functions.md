---
tags:
  - programming
  - bash
---
```bash
function_name {
	command
}
```
# Example
```bash
myfunction() {
	arg1=$1
	arg2=$2
	echo $(($1 + $2))
	return 0
}
globalvar = "hello"
myfunction 1 2
```