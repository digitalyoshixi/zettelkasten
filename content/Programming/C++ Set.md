---
tags:
  - programming
  - cpp
---
An ordered list with elements that appear only once
# Boilerplate
```cpp
#include <set>
set<string> cars;
set<string> cars = {"Volvo", "BMW", "Ford", "Mazda"};
// Add new elements
cars.insert("Tesla");
// Remove elements
cars.erase("Volvo");
cout << cars.size();  // Outputs 4
// Remove all elements
cars.clear();
if (cars.contains("Tesla")){
	cout << "yes,there is a tesla";
}
```