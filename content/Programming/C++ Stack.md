---
tags:
  - programming
  - cpp
---
# Boilerplate
```cpp
#include <stack>
int main(){
	std::stack<int> st;
	st.push(10);
	cout << "top element: " << st.top() << '\n';
	st.pop();
	return 0;
	cout << "size: " << st.size() << '\n';
}
```