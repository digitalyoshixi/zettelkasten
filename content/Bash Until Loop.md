---
tags:
  - programming
  - bash
---
```bash
until [ condition ]; do
	command...
done
```
- Keeps looping as long as condition is false
# Example
```bash
COUNT=1
until [ $COUNT -gt 5 ]; do
	echo "$COUNT"
	COUNT=$(($COUNT + 1))
```