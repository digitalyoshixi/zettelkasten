---
tags:
  - programming
---
A [[Leetcode]] hashing problem.
# Question
https://leetcode.com/problems/group-anagrams
# Soln
```cpp
vector<short> customhash(string &str){
  vector<short> ret(26, 0);
  for (char c : str){
    ret[c-'a'] +=1;
  }
  return ret;
}

vector<vector<string>> groupAnagrams(vector<string>& strs) {
  // create hashmap
  map<vector<short>, vector<string>> arrtoindex;
  for (int i = 0; i < strs.size(); i++){
    // compute hash
    vector<short> hash = customhash(strs[i]);
    // map into hashmap
    if (arrtoindex.find(hash) != arrtoindex.end()){
      //vector<string> res = arrtoindex[hash];
      arrtoindex[hash].push_back(strs[i]);
    }
    else{
      arrtoindex[hash] = {strs[i]};
    }
  }
  // return the results of the map
  vector<vector<string>> retvec;
  for (auto it : arrtoindex){
    vector<string> templist;
    for (string i : it.second){
      templist.push_back(i);
    }
    retvec.push_back(templist);
  }
  return retvec;
}
```