---
tags:
  - cpp
---
These are dynamic arrays in C++
# Usage
```cpp
#include <vector>

vector<string> cars;
vector<string> carsfixedsize(3,0); // init 3 to 0
vector<string> cars2 = {"Volve", "BMW", "Ford"};

for (string car : cars2){
	cout << car << "\n";
}
cout << cars2[0]; // returns 1st element
cout << cars2[1]; // returns 2st element
cout << cars2.at(0); // returns 1st element and handles errors
cout << cars2.at(9); // returns 9th element and handles errors
cars2[0] = "Medio" // modify value
cout << cars2.front(); // first element
cout << cars2.back(); // last element
cars2.push_back("Mazda"); // add a element to the back
cars2.pop_back(); // remove an element to the back
cars2.size() // returns the length of the vector
cars2.erase(0)
```