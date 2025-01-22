---
tags:
  - cpp
---
endl does 2 things:
- write a line feed/new line character
- flush the [[Buffered outputs]]
We can print new line
```cpp
std::cout << "Hi" << std::endl; // Hi\n
```
It is best practice to output with newlines for every line if possible

# Obsolensce
it is just better to use `\n` instead.
1. its better to let the system flush the buffers periodically(which it is designed to do efficiently)
2. shorter, easier to remember