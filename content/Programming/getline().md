---
tags:
  - cpp
---
# For user input
takes 2 arguments. First is the input stream, then its the variable.
```cpp
std::string name{};
    std::getline(std::cin >> std::ws, name); // read a full line of text into name
```
[[ws|std::ws]] will remove whitespace

returns the length of the line gotten.

