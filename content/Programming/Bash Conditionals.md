---
tags:
  - programming
  - bash
---
```bash
if [ condition ]; then
	action
elif [ condition ]; then
	action
else
	action
fi
```
# Examples
### Example 1
```sh
if grep Ford students
then
	echo end of list
else
	echo No student named ford
fi
```
### Example 2
```sh
if test $x -lt 3
then
	echo this is very suprising
fi
```
### Example 3
```bash
if [ $# -lt 1 ] then
	echo "mymsg"
fi
```