---
tags:
  - cpp
---
# Boilerplate
```cpp
#include <set>
unordered_set<string> cars;
set<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};
// Add new elements
cars.insert("Tesla");
// Remove elements
cars.erase("Volvo");
cout << cars.size();  // Outputs 4
// Remove all elements
cars.clear();
```