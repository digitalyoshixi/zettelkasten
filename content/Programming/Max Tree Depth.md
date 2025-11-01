---
tags:
  - programming
---
A [[Leetcode]] [[Tree]] problem
# Problem
https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Soln
```cpp
int maxDepth(TreeNode* root) {
  if (root == nullptr) return 0;
  int leftdepth = maxDepth(root->left);
  int rightdepth = maxDepth(root->right);
  if (root == nullptr && leftdepth == 0 && rightdepth == 0) return 0;
  if (leftdepth > rightdepth) return 1 + leftdepth;
  else return 1 + rightdepth;
}
```