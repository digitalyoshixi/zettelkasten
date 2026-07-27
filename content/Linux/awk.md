---
tags:
  - programming
  - bash
  - linux
---
A programming language that will be able to modify raw text.
# Getting First Field
```
cat /etc/passwd | awk -F: '{print $1 }'
```
Where the fields are split by `SPACE`
```
cat /etc/passwd | awk -F: '$1 == "dave" {print $7 }'
```