---
tags:
  - programming
  - bash
---
```bash
$# # number of arguments given
$0 # command name
$1 # first argument
$2 # second argument
$* # all arguments space seperated
$@ # all arguments except $0 space seperated
```
# Example
```bash
#!/bin/bash

echo $@
echo $0
echo $1
echo $2
```
![[Bash Arguments-20260414234328737.webp]]
# Iterating Over All Arguments
```bash
#!/bin/bash
for arg in "$@"; do
	echo $arg
done
```