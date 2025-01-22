---
tags:
  - cpp
---
`setw(int width)`
For output formatting. makes sure the next character outputted has indentation exactly at the width given.
# Example
```cpp
 std::cout << std::setw(16) << "bool:" << sizeof(bool) << " bytes\n";
```
output:
`bool:           1 bytes`