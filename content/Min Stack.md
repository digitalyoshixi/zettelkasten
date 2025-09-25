---
tags:
  - programming
---
A data structure similar to a [[Stack]], but you can retrieve the minimum value at any time.
Also a [[Leetcode]] medium.
# Problem
https://leetcode.com/problems/min-stack/
# Implementation
```cpp
class MinStack {
public:
    stack<int> st;
    stack<int> minst;
    MinStack() {
    }
    
    void push(int val) {
      st.push(val);
      if (minst.size() == 0){
        minst.push(val);
        return;
      }
      if (val < minst.top()) {
        minst.push(val);
      }
      else {
        minst.push(minst.top());
      }
    }
    
    void pop() {
      minst.pop();
      st.pop();
    }
    
    int top() {
      return st.top();
    }
    
    int getMin() {
      return minst.top();
    }
};
```