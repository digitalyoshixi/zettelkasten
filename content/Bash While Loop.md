---
tags:
  - programming
  - bash
---
```bash
while [ condition ]; do
	command...
done	
```
# Example
```bash
COUNT=4
while [ $COUNT -gt 0 ]; do
	echo "$COUNT"
	COUNT=$(($COUNT-1))
done
```