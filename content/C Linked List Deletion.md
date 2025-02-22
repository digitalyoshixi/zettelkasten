---
tags:
  - c
  - programming
---
```c
void delete_linked_list(Node *head){
	Node *p = head;
	Node *q = NULL;
	while (p != NULL){
		q = p->next;
		free(p);
		p = q;
	}
}
```