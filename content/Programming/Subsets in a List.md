---
tags:
  - programming
---
A [[Leetcode]] problem involving [[Backtracking]].
# Problem
https://leetcode.com/problems/subsets/
# Solution
```cpp
#include "leetcodeutils.hpp"
using namespace std;


vector<vector<int>> subsetsrec(vector<int>& nums, int index, vector<int>& orig){
  vector<vector<int>> retlist;
  vector<int> origcopy = orig;
  origcopy.push_back(nums[index]);
  retlist.push_back(origcopy);
  for (int i = index+1; i < nums.size(); i++){
    vector<vector<int>> templist = subsetsrec(nums, i, origcopy);
    retlist.insert(retlist.end(), templist.begin(), templist.end());
  }
  return retlist;
}

vector<vector<int>> subsets(vector<int>& nums) {
  vector<vector<int>> retlist = { {} };
  for (int i = 0; i < nums.size(); i++){
    vector<int> empty = {};
    vector<vector<int>> templist = subsetsrec(nums, i, empty);
    retlist.insert(retlist.end(), templist.begin(), templist.end());
  }
  return retlist;
}

int main(){
  vector<int> a = {1,2,3};
  vector<vector<int>> res = subsets(a);
  for (int i = 0; i < res.size(); i++){
    cout << "[" ;
    for (int j = 0; j < res[i].size(); j++){
      cout << res[i][j] << ",";
    }
    cout << "]," ;
  }
  cout << "\n";
}
```