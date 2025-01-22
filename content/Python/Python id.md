---
tags:
  - python
---
For each new literal not already in memory, a new id is made.
For example:
```python
a = 5
a = 3
```
Will make 2 ids. One of the ids will be the memory cell of 5, another will be the memory cell of 3.
# id() function
`id(<variablename>)` will return an integer representing the "memory address" of the variable.
