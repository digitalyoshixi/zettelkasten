---
tags:
  - programming
  - bash
---
```bash
for arg in list do
	command
done
```
# Examples
### Example 1
```bash
for i in 1 2 3 4; do
	echo $i
done
```
### Example 2
```bash
for f in `ls`; do
	cat $f
done
```
### Example 3
```bash
for i in `seq 10`; do
	cat $i
done
```