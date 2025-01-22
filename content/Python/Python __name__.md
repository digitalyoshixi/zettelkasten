---
tags:
  - python
---
A string corresponding to the filename of the module or current file.
# `__main__`
The default built-in.
```python
print(__name__) # __main__
```
# `__somemodulename__`
```python
import animals
print(animals.__name__) # animals
```