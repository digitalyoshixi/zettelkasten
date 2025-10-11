---
tags:
  - programming
  - cpp
aliases:
  - C++ Hashmap
---
# Boilerplate
```cpp'
#include <unordered_map>
unordered_map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} }; 

// access value at location
int boage = people["Bo"]
// access with exceptions if does not exist
int boagesafe = people.at("Kenny"); 
// check if item exists in hashmap
// if (people.find("f") != people.end()) cout << "exists";
if (m.count(key)) cout << "exists";

// set new value
people["Daniel"] = 20;

// remove a key-value pair
m.erase("Daniel") 

// Print the key-value pairs
for (auto it : people)
	cout << it.first << " " << it.second << endl;


```