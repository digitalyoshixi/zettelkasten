---
tags:
  - python
---
A style checker for python code.
It is part of python [[Code Linting]]
# Statement Types
### Pointless Statement
If a statement can be removed, or added to another previous statement without change to the program.
```python
result = a + b;
result * c; # this does nothing
return result;
```
### Unreachable Statement
Statements that are after return values.
```python
return "ended ok?";
print("i am not going to run");
```
### Unused Argument
If a required parameter is unused.
### Undefined Variable
A variable is used without being defined beforehand
```python
print(banwa)
```
### Redefined Builtin
If any variable or function name shares a similar name to any [[Python __builtins__]]
### Unexpected Indent
Python cares about indentation for its syntax
### Redefined Outername
When the function name is defined as another value.
```python
total(num1, num2):
	total = num1 + num2
	return total
```
