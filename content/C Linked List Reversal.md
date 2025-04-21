---
tags:
  - programming
  - c
---
```c
#include <stdio.h>
#include <stdlib.h>

typedef struct LL_Node_Struct{
  int val;
  struct LL_Node_Struct *next;
}LL_Node;

LL_Node *create_node(int val){
  LL_Node *temp = (LL_Node*)calloc(1, sizeof(LL_Node));
  temp->val = val;
  temp->next = NULL;
  return temp;
}

LL_Node *add_node(LL_Node *head, int val){
  LL_Node *curr = head;
  if (curr == NULL){
    return NULL;
  }
  while (curr->next != NULL){
    curr = curr->next;
  }
  // new node 
  LL_Node *new_node = create_node(val);
  curr->next = new_node;
  return head;
}

void print_ll(LL_Node *head){
  LL_Node *curr = head;
  while (curr != NULL){
    printf("%d, ", curr->val);
    curr=curr->next;
  }
  printf("\n");
}

LL_Node *reverse_ll(LL_Node *head){
  if (head == NULL){
    return NULL;
  }
  LL_Node *curr = head->next;
  LL_Node *curr_prev = head;
  while (curr != NULL){
    LL_Node *b = curr->next;
    LL_Node *a = curr;
    curr->next = curr_prev;
    if (curr_prev->next == a){
      curr_prev->next = NULL;
    }
    curr = b;
    curr_prev = a;
  }
  return curr_prev;
}

int main(){
  LL_Node *head =  create_node(20);
  add_node(head, 30);
  add_node(head, 21);
  add_node(head, 32);
  add_node(head, 45);
  print_ll(head);
  head = reverse_ll(head);
  print_ll(head);
  return 0;
}
```