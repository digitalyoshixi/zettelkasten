---
tags:
  - programming
---
A [[Leetcode]] problem involving [[Binary Search]].
# Problem
https://leetcode.com/problems/median-of-two-sorted-arrays/
# Soln
```cpp
#include "leetcodeutils.hpp"
using namespace std;


double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    vector<double> newarray;
    int midindex = (nums1.size()+nums2.size())/2;
    int parity = (nums1.size()+nums2.size()) % 2;
    double prev = 0;
    int left = 0;
    int right = 0;
    while (left < nums1.size() & right < nums2.size()){
      if (nums1[left] < nums2[right]){
        if (left+right == midindex & parity == 1) return nums1[left];
        if (left+right == midindex-1 & parity == 0) prev = nums1[left];
        if (left+right == midindex & parity == 0) return (nums1[left] + prev) / 2;
        newarray.push_back(nums1[left++]);
      }
      else{
        if (left+right == midindex & parity == 1) return nums2[right];
        if (left+right == midindex-1 & parity == 0) prev = nums2[right];
        if (left+right == midindex & parity == 0) return (nums2[right] + prev) / 2;
        newarray.push_back(nums2[right++]);
      }
    }
    while (left < nums1.size()){
      if (left+right == midindex & parity == 1) return nums1[left];
      if (left+right == midindex-1 & parity == 0) prev = nums1[left];
      if (left+right == midindex & parity == 0) return (nums1[left] + prev) / 2;
      newarray.push_back(nums1[left++]);
    }
    while (right < nums2.size()){
      if (left+right == midindex & parity == 1) return nums2[right];
      if (left+right == midindex-1 & parity == 0) prev = nums2[right];
      if (left+right == midindex & parity == 0) return (nums2[right] + prev) / 2;
      newarray.push_back(nums2[right++]);
    }
    return 0;
}

int main(){
  vector<int> left = {1,2};
  vector<int> right = {3,4};
  double res = findMedianSortedArrays(left, right);
  cout << res;
}

```