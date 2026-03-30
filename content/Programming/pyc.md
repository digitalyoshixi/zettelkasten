---
tags:
  - programming
  - python
---
A compiled python program that contains [[Python Bytecode]] to run.
Oftentimes used as cached program, so the interpreter doesn't need to reparse the code.
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
# Decompiling
- https://www.pylingual.io/3