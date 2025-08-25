---
tags:
  - programming
  - dynamic_programming
---
A [[Leetcode]] [[Dynamic Programming|DP]] question
# Question
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
# Soln
```cpp
#include <iostream>
#include <vector>
using namespace std;

int maxProfit(vector<int>& prices) {
  int smallestvalue = prices[0];
  int largestvalue = prices[0];
  int pastsum = 0;
  for (int i = 0; i < prices.size(); i++){
    if (prices[i] <= smallestvalue){
      smallestvalue = prices[i];
      largestvalue = prices[i];
    }
    else if (prices[i] > largestvalue){
      largestvalue = prices[i];
    }
    if (largestvalue- smallestvalue > pastsum){
      pastsum = largestvalue- smallestvalue;
    }
  }
  return pastsum;
}

int main(){
  vector<int> myprices = {2,1, 4};
  cout << maxProfit(myprices) << '\n';
  myprices = {1,2};
  cout << maxProfit(myprices) << '\n';
  myprices = {2,1};
  cout << maxProfit(myprices) << '\n';
  myprices = {2,4,1};
  cout << maxProfit(myprices) << '\n';
}
```