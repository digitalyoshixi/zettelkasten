---
tags:
  - programming
  - python
---
A compiled python program that contains [[Python Bytecode]] to run.
# Compiling
```
python -m compileall <file>.py
```
Result is now in `__pycache__`
# Running
```
python myfile.pyc
```
# Executing with [[Python Marshal]]
```python
marshal.loads()
#Takes in a bytes object of the pyc object code
```