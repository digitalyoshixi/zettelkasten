---
tags:
  - cpp
---
# Implicit
Compiler does this automatically 
example is integer->double. It can do this easily.
sometimes it will also allow 'unsafe' operations like double->integer

# Explicit
use the `static_cast` operator
`static_cast<new_type>(expression)`
```cpp
std::cout << static_cast<int>(5.5); // explicitly convert double value 5.5 to an int
```
