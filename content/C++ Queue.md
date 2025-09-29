---
tags:
  - programming
  - cpp
---
```cpp
#include <queue>

int main(){
	queue<int> q;
	q.push(10); // insert element at end
	cout << q.front() << endl;
	cout << q.back() << endl;
	q.pop(); // remove element at front
	return 0;
}
```