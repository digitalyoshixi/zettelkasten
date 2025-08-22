---
tags:
  - programming
  - cpp
---
# Boilerplate
```cpp
map<string, int> people = { {"John", 32}, {"Adele", 45}, {"Bo", 29} }; 

// access value at location
int boage = people["Bo"]
// access with exceptions if does not exist
int boagesafe = people.at("Kenny"); 
// set new value
people["Daniel"] = 20;
```