---
tags:
  - programming
---
A [[Leetcode]] problem about [[Linked List]]
# Problem
https://leetcode.com/problems/add-two-numbers/
# Soln
```

ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    struct ListNode* root = new ListNode();
    struct ListNode* curr = nullptr;
    int carry = 0;
    while (l1 != nullptr | l2 != nullptr | carry != 0){
        int left = 0;
        int right = 0;
        if (l1 != nullptr){
          left = l1->val;
          l1 = l1->next;
        } 
        if (l2 != nullptr){
          right = l2->val;
          l2 = l2->next;
        }
        int newcarry = (left+right+carry) / 10;
        int res = (left+right+carry) % 10;
        carry = newcarry;
        if (curr == nullptr){
            root->val = res;
            root->next = nullptr;
            curr = root;
        }
        else {
            struct ListNode* next = new ListNode(res);
            curr->next = next;
            curr = curr->next;
        }
    }
    return root;
}
```