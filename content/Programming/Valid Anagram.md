---
tags:
  - programming
---
A [[Leetcode]] problem on lists.
# Problem
https://leetcode.com/problems/valid-anagram/
# Soln
Develop a [[Hashing|Hashing Algorithms]]
```cpp
#include <iostream>
#include "math.h"
#include <bits/stdc++.h>
#include <vector>
#include <list>
#include <set>
using namespace std;

bool isAnagram(string s, string t) {
    if (s.size() != t.size()) return 0;
    long long ssum = 0;
    long long tsum = 0;
    for (int i = 0; i < s.size(); i++){
        ssum += pow(2,s[i]-91)-s[i];
        tsum += pow(2,t[i]-91)-t[i];
    }
    return ssum == tsum;
    
}

int main(){
  cout << isAnagram("dcccc", "bbbbe");
}
```
# Neetcode Soln
```cpp
 bool isAnagram(string s, string t) {
        if (s.length() != t.length()) {
            return false;
        }

        vector<int> count(26, 0);
        for (int i = 0; i < s.length(); i++) {
            count[s[i] - 'a']++;
            count[t[i] - 'a']--;
        }

        for (int val : count) {
            if (val != 0) {
                return false;
            }
        }
        return true;
    }
```