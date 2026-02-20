---
tags:
  - programming
  - cpp
---
```cpp
#include <tuple>

int main(){
	std::tuple<int, int>{1,1};
	std::tuple<int, int> mytup = std::make_tuple(1,1);
	get<0>(mytup) = 2;
	cout << get<1>(mytup);
	return 0;
}
```