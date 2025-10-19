---
tags:
  - programming
  - python
---
A special function that allows you to modify the behavior of a function without changing the underlying code. Similar to [[Higher Order Function]].
Often starts with an `@` sign.
# Example
```python
def hello(func):
	def inner():
	    print("Hello ")
	    func()
	return inner
	
@hello 
def name():
	print("Alice")
```