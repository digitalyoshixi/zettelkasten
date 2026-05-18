---
tags:
  - programming
  - bash
  - linux
aliases:
  - sed
---
A find and replace program for [[Unix]] systems.
# Usage
```
sed 's/FUCK/####/'
```
- Replaces all instances of `FUCK` with `####`
### Multiple Expressions
```
sed -e 's/d..e/buddy/' -e 's/bash/fish/'
```