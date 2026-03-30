---
tags:
  - programming
  - cpp
---
The ability to define different function behavior.
# Alternate Body For Input Type
```cpp
#include <iostream>
#include <cstring>
#include <type_traits>

// a function that takes input type T, returns bool if fn is null
template <typename T> bool check_null(T input) { 
    if constexpr(std::is_same_v<T,int>) {
         return (0 == input);
    } 
    else if constexpr(std::is_same_v<T,std::string>) {
         return input.compare("") == 0;
    }
    return false;
}

int main(){
  std::cout << check_null<int>(20) << "\n"; // false(0)
  std::cout << check_null<int>(0)<< "\n"; // true(1)
  std::cout << check_null<std::string>("aas")<< "\n"; // false(0)
  std::cout << check_null<std::string>("")<< "\n"; // true(1)
  return 0;
}

```