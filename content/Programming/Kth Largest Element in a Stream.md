---
tags:
  - programming
---
A [[Leetcode]] [[Min-Heap]] problem.
# Problem
https://leetcode.com/problems/kth-largest-element-in-a-stream/
# Soln
```cpp
vector<int> merge(vector<int> l, vector<int> r){

vector<int> ret;

int lptr = 0;

int rptr = 0;

while (lptr < l.size() && rptr < r.size()){

if (l[lptr] > r[rptr]) ret.push_back(l[lptr++]);

else ret.push_back(r[rptr++]);

}

while (lptr < l.size()){

ret.push_back(l[lptr++]);

}

while (rptr < r.size()){

ret.push_back(r[rptr++]);

}

return ret;

}

  

vector<int> mergesort(vector<int> arr){

if (arr.size() <= 1) return arr;

int mid = arr.size()/2;

vector<int> l;

vector<int> r;

for (int i = 0; i < arr.size(); i++){

if (i < mid) l.push_back(arr[i]);

else r.push_back(arr[i]);

}

l = mergesort(l);

r = mergesort(r);

return merge(l,r);

}

  
  

class KthLargest {

public:

vector<int> nums;

int k = 0;

KthLargest(int k, vector<int>& nums) {

this->nums = mergesort(nums);

this->k = k;

}

int add(int val) {

bool inserted = false;

for (int i = 0; i < nums.size(); i++){

if (val > nums[i]){

nums.insert(nums.begin() + i, val);

inserted = true;

break;
}
}

if (inserted == false) nums.push_back(val);
return nums[k-1];
}
};
```