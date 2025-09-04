---
tags:
  - programming
  - python
---
# Boilerplate
```python
import re

txt = "The rain in Spain"
x = re.findall(r"ai", txt)
print(x)
x = re.search(r"\s", txt)
if x != None:
	print("There is an occurance of whitespace")
```