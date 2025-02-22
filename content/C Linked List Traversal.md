---
tags:
  - c
  - programming
---
```c
void linked_list_traversal(Node *head){
	Node *p = head;
	while (p != NULL){
		printf("%p", p);
		p = p->next;
	}
}
```