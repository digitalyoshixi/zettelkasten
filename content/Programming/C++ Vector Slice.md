---
tags:
  - programming
---
```cpp
// slice from [2:4]
vector<int> v = {1,2,3,4,5,6};
auto first = v.begin() + 2;
auto last = v.begin() + 4;
// Copy the element
vector<int> sliced(first, last); // {3,4}
```