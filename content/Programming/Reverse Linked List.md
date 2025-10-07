---
tags:
  - programming
---
A [[Leetcode]] problem involving [[Linked List]].
# Problem
https://leetcode.com/problems/reverse-linked-list
# Soln
```cpp
#include "leetcode.hpp"

using namespace std;

ListNode* reverseList(ListNode* head) {
  ListNode* next = head->next;
  if (next == nullptr){
    return head;
  }
  ListNode* rethead = reverseList(head->next);
  next->next = head;
  // last case
  head->next = nullptr;
  return rethead;
}

int main(){
  ListNode* a = new ListNode(1);
  ListNode* b = new ListNode(2);
  ListNode* c = new ListNode(3);
  ListNode* d = new ListNode(4);
  ListNode* e = new ListNode(5);
  a->next=b;
  b->next=c;
  c->next=d;
  d->next=e;
  ListNode* res = reverseList(a);
  cout << res->val;
}
```