---
tags:
  - programming
  - cpp
---
A object that allows traversing of a sequence one-by-one.
```cpp
vector<int> numbers = {1,2,3,1,4,6};
vector<int>::iterator it;
it = numbers.begin();
cout << *it << '\n'; // print the element at the iterator (1)
it++; // go to next element
while (it < numbers.end()){
	cout << *it << '\n';
	it++;
}
```