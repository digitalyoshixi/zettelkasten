---
tags:
  - programming
aliases:
  - Last In First Out
  - LIFO
  - FILO
  - First In Last Out
---
A [[Abstract Data Type|ADT]] that follows [[Stack|LIFO]] principle.
Able to push and pop values.
![[Stack-20251023160413772.webp]]
# Data Structure
```cpp
class myStack {
    // array to store elements
    int *arr;       
    // maximum size of stack
    int capacity;   
    // index of top element
    int top;          
public:
    // constructor
    myStack(int cap) {
        capacity = cap;
        arr = new int[capacity];
        top = -1;
    }
};
```