---
tags:
  - programming
  - competitive_programming
---
# My Header File
```cpp
#pragma once
#include <iostream>
#include "math.h"
#include <bits/stdc++.h>
#include <vector>
#include <unordered_map>
#include <list>
#include <set>
#include <stack>
#include <string>
#include <map>
#include "stdlib.h"

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

```
# Dynamic Programming
- [[Climbing Stairs]]