---
tags:
  - nix
---
These are the equivalent of [[Hash Map|Hash Maps]] or [[Python Dictionary|Python Dictionaries]] for [[Nix]].
# Writing Methods
### = for children
```python
x = {
	one = "hello";
	two = "world";
	three = 9;
}
```
### . for children
```python
x.one = "hello";
x.two = "world";
x.three = 9;
```
### = to a set
```python
x = {one = "hello"};
x = {two = "world"};
x = {three = 9};
```
# Reading Children
```c
x.one
// > "hello"
```
