---
tags:
  - programming
  - c
---
```make
target [target2 ... ]: dep1 dep2 ...
	action1
	...
	actionn
```
# Dependency Checking
1. Will check if a rule exists for dependency
2. Will check if environment variable contains dependency
3. Will check if local directory contains file with dependency