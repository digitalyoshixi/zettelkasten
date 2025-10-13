---
tags:
  - programming
  - python
---
A keyword used to create [[Python Generator|Python Generators]].
# Example
```python
def fun(m):
    for i in range(m):
        yield i  

# call the generator function
g = my_generator(5)
for i in range(5):
	print(next(g))
# Alternative reading
# for n in fun(5):
#     print(n)
```