---
tags:
  - python
---
Can create or get the attribute of python object.
# Getting Attribute
```python
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'age') # will be 36
```
# Creating Attribute
```python
class Person:
  name = "John"
  age = 36
  country = "Norway"

x = getattr(Person, 'page', 'my message')

print(x) # will be 'my message'
```
