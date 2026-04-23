---
tags:
  - programming
  - bash
---
```bash
case "$variable" in
	"$condition1" ) command;;
	"$condition2" ) command;;
esac
```
# Example
```bash
mycase=1
case $mycase in
	1) echo "bash";;
	2) echo "perl";;
	3) echo "python";;
	4) echo "c++";;
	5) exit
esac
```