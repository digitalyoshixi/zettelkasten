---
tags:
  - programming
  - dynamic_programming
---
Any algorithm that satisfies the problem at the earliest instant possible, ending prematurely.
They do not follow [[Dynamic Programming]] practices.
# Examples
A greedy algorithm for house robber would not work
```
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.  
  
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
```
In the case of [2.7.9.3.1] as an input, the gredy algo would choose [7,3] which is not the correct output