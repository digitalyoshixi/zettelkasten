---
tags:
  - programming
---
A [[Leetcode]] [[Binary Tree]] problem.
# Problem
https://leetcode.com/problems/invert-binary-tree/
# Soln
```cpp
TreeNode* invertTree(TreeNode* root) {
  if (root != nullptr){
    root->left = invertTree(root->left);
    root->right = invertTree(root->right);
    TreeNode* temp = root->left;
    root->left = root->right;
    root->right = temp;
  }
  return root;
}
```