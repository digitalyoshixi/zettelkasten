---
tags:
  - python
aliases:
  - Python Datatype
---
# Retrieving Data Type
```python
x = 5
print(type(x))
```
# Typecasting
```python
r = 2.3921
a = int(r)
```
# Primitive
| Datatype   | Use-case                              |
| ---------- | ------------------------------------- |
| byte       | 1 byte                                |
| short      | 2 bytes                               |
| int        | 4 bytes                               |
| char       | 4 bytes. single ascii character       |
| long       | 8 bytes                               |
| float      | a float with wordsize                 |
| double     | a float with length of twice wordsize |
| boolean    | 1 byte. true or false flag            |
| bytes      | the bytes representation              |
| bytearray  | array of bytes from a string          |
| memoryview | a buffer                              |
| NoneType   | no type at all                        |
Also includes the [[C Datatypes]] through the `ctypes` library
# Advanced
| Datatype  | Use-case                                                     |
| --------- | ------------------------------------------------------------ |
| str       | holds unlimited due to [[Polymerization]]. holds string data |
| complex   | complex numbers like $i$                                     |
| list      | non-uniform array. a list of varying types                   |
| tuple     | tuple of values                                              |
| range     | integer array                                                |
| dict      | a key-value mapping                                          |
| set       | set of values                                                |
| frozenset | immutable set                                                |
|           |                                                              |
