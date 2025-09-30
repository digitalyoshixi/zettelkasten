---
tags:
  - programming
---
A leetcode problem about substrings
# Problem
https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Solution
```cpp
#include "leetcodeutils.hpp"
using namespace std;

int lengthOfLongestSubstring(string s) {
        if (s.size() <= 1) return s.size();
        int max = 1;
        int left = 0;
        int right = 1;
        unordered_set<char> seen;
        seen.insert(s[0]);
        while (right < s.size()){
            if (seen.contains(s[right])){
                seen.erase(s[left]);
                left++;
            }
            else{
                seen.insert(s[right]);
                int newsum = right-left+1;
                if (newsum > max) max = newsum;
                right++;
            }
        }
        return max;
    }

int main(){
  string s = "aab";
  cout << lengthOfLongestSubstring(s);
}

```