---
tags:
  - python
---
`string[<start>:<end>:<step>]`
end is exclusive.
start is inclusive
Creates a copy.
Since the end is exclusive, if you had the start and end be the same like `str[2:2]`, it would return `''` as the end is omitted.

# Overslicing
```python
mylist = ['a','b']
print(mylist[0:2]) # ['a','b']
```
overslicing will not add any new values