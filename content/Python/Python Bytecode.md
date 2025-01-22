---
tags:
  - python
aliases:
  - Python Assembly
---
Can be viewed with [[Python dis]].
![[Python Bytecode-20240912182510642.webp]]
# Full List
https://docs.python.org/3/library/dis.html#python-bytecode-instructions
1. LOAD_CONST: Pushes a constant onto the stack.
2. LOAD_FAST: Loads a local variable onto the stack.
3. STORE_FAST: Stores a value into a local variable.
4. LOAD_GLOBAL: Loads a global variable onto the stack.
5. CALL_FUNCTION: Calls a function.
6. RETURN_VALUE: Returns a value from a function.
7. POP_TOP: Removes the top item from the stack.
8. JUMP_ABSOLUTE: Jumps to an absolute target.
9. COMPARE_OP: Performs a comparison operation.
10. BINARY_ADD: Implements the addition operation.
11. BINARY_MULTIPLY: Implements the multiplication operation.
12. LOAD_ATTR: Loads an attribute from an object.
13. STORE_ATTR: Stores an attribute in an object.
14. BUILD_LIST: Creates a new list.
15. BUILD_TUPLE: Creates a new tuple