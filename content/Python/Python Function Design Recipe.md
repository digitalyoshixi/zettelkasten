---
tags:
  - python
---
1. Write example uses. Dont add extra spaces before/after the output
```python
	"""
    >>> 	testfunc(2)
	2
    >>> 	testfunc(5)
	5
	"""
```
2. Write function header and add the [[Python Docstring]] immediately after the header. Ensure there is a [[Python Docstring|Precondition]]
```python
def testfunc(input : int) -> int:
	"""
	returns the input function
    >>> 	testfunc(2)
	2
    >>> 	testfunc(5)
	5
	"""
```
The header can have a [[Return Annotation]], but it is not required
1. Write function description
```python
def testfunc(input):
	""" returns the user's input
	returns the input function
    >>> 	testfunc(2)
	2
    >>> 	testfunc(5)
	5
	"""
```
4. Write the body
```python
def testfunc(input):
	"""
	returns the input function
    >>> 	testfunc(2)
	2
    >>> 	testfunc(5)
	5
	"""
	return input
```
5. Test the function with [[Python Doctest]]