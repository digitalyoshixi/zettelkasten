---
tags:
  - programming
---
A [[Data Structures and Algorithms|Data Structures]] that uses an array like a [[Hashmap]].
Each index is for a specific key.
# Example
[[Valid Anagram]]
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