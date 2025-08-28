---
tags:
  - programming
  - python
---
# Boilerplate
```python
import re

txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
x = re.search("\s", txt)
if x != None:
	print("There is an occurance of whitespace")
```