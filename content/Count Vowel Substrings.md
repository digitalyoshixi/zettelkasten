---
tags:
  - programming
---
A [[Leetcode]] problem involving [[Sliding Window]]
# Problem
https://leetcode.com/problems/count-vowel-substrings-of-a-string/
# Soln
```cpp
#include "leetcodeutils.hpp"
using namespace std;

bool checkFullVowel(map<char,int> occurances){
  return occurances['a'] > 0 && occurances['e'] > 0 &&occurances['i'] > 0 &&occurances['o'] > 0 && occurances['u'] > 0;
}

bool checkVowel(char c){
  return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int countVowelSubstrings(string word) {
  int counts=0;
  map<char, int> occurances = {
    {'a', 0},
    {'e', 0},
    {'i', 0},
    {'o', 0},
    {'u', 0}
  };
  int left = 0;
  int right = 0;
  while (right <= word.size()){
    int origleft = left;
    while (left < right && checkFullVowel(occurances)){
      counts++;
      occurances[word[left]]--;
      left++;
    }
    while (left > origleft){
      left--;
      occurances[word[left]]++;
    }
    if (right < word.size() && checkVowel(word[right])){
      occurances[word[right]]++;
    }
    else{
      left = right+1;
      occurances = {
        {'a', 0},
        {'e', 0},
        {'i', 0},
        {'o', 0},
        {'u', 0}
      };
    }
    right++;
  }
  return counts;
}
int main(){
  cout << countVowelSubstrings("bbaeixoubb");
}

```