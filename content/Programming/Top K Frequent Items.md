---
tags:
  - programming
---
A leetcode problem involving [[Bucket Sort]]
# Problem
https://leetcode.com/problems/top-k-frequent-elements
# Soln
```cpp
#include <iostream>
#include "math.h"
#include <bits/stdc++.h>
#include <vector>
#include <unordered_map>
#include <list>
#include <set>
using namespace std;

vector<int> topKFrequent(vector<int>& nums, int k) {
    vector<int> retvec;
    int totalunique = 0;
    unordered_map<int, int> freqmap;
    for (int n : nums){
      if (freqmap.find(n) == freqmap.end()) totalunique++;
      freqmap[n] += 1;
    }
    // order hashmap into bucketlist
    vector<vector<int>> buckets(totalunique+1);
    for (auto it : freqmap)
      buckets[it.second-1].push_back(it.first);

    // return the last few items
    int totalreturned = 0;
    for (int i = totalunique; i >= 0; i--){
      if (totalreturned == k) break;
      for (int v = 0; v < buckets[i].size(); v++){
        if (totalreturned == k) break;
        retvec.push_back(buckets[i][v]);
        totalreturned++;
      }
    }
    return retvec;
}

int main(){
  //vector<string> mystringvec ={"eat","tea","tan","ate","nat","bat"};
  vector<int> myinp = {1,2,1,2,1,2,3,1,3,2};
  vector<int> res = topKFrequent(myinp, 2);
  for (int c : res){
    cout << c << ",";
  }
}

```