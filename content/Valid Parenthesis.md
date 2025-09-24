---
tags:
  - programming
---
A [[Leetcode]] problem about [[Stack]]
# Problem
https://leetcode.com/problems/valid-parentheses/
# Soln
```cpp
bool isValid(string s) {
        std::stack<int> st;
        for (int i = 0; i < s.size(); i++){
            char c = s[i];
            if (st.size() > 0){
              if (c == '}' & st.top() == '{'){
                  st.pop();
              }
              else if (c == ')' & st.top() == '('){
                  st.pop();
              }
              else if (c == ']' & st.top() == '['){
                  st.pop();
              }
              else {
                  st.push(c);
              }
            }
            else {
                st.push(c);
            }
        }
        return st.size() == 0;
}    

```