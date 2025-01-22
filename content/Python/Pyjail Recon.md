---
tags:
  - python
  - jail
---
### Recon
##### Checking Builtins
```python
import builtins
print(dir(builtins))
```
##### Checking Keywords
```python
import keyword
print(keyword.kwlist)
```
##### Checking Global Variables
```python
print(globals())
```
##### Checking Local Variables
```python
print(locals())
```
##### Checking Internal Attributes
```python
# for subclasses. (require you have an object)
print(object.__subclasses__())

# for __globals__ (require you have a function)
def some_function():
    pass
print(some_function.__globals__)

# for __self__ (requires you have a class)
class SomeClass:
    def some_method(self):
        pass
obj = SomeClass()
print(obj.some_method.__self__)

# for __builtins__
print(__builtins__)
# for __spec__
import sys
print(sys.__spec__)
```