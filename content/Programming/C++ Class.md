---
tags:
  - programming
  - cpp
---
C++ classes.
# Concepts
- [[C++ Constructor]]
- [[C++ Destructor]]
- [[C++ Private]]
- [[C++ Virtual]]
# Example
### CPP File
```cpp
#include "StringList.h"
void StringList::insert_string(char string[1024])
{
	// Insert a new string into the linked list
	// at the head of the list (for simplicity)
	ListNode *p=new ListNode; // This is how we dynamically
	// allocate data on-demand in C++
	// (no need for calloc)
	if (p==NULL)
	{
		printf("There is no memory for more strings!\n");
		return;
	}
	strcpy(&p->string[0],string);
	if (this->head==NULL) // ’this’ is a pointer to
	{ // the specific object for
		this->head=p; // which the function was called
		this->list_length++;
		return;
	}
	else
	{
		p->next=this->head;
		this->head=p;
		this->list_length++;
		return;
	}
}
void StringList::delete_string(char string[1024])
{
// Deletes a string from the linked list if it
	ListNode *p, *q;
	p=this->head;
	// If requested string is at the head of the list
	if (strcmp(p->string,string)==0)
	{
		this->head=this->head->next;
		this->list_length--;
		delete p;
		return;
	}
	// Otherwise
	while(p->next!=NULL)
	{
		q=p->next;
		if (strcmp(q->string,string)==0)
		{
			p->next=q->next;
			delete q;
			this->list_length--;
		}
		p=q;
	}
}
void StringList::print_strings(void)
{
	// Print out all the strings currently in the list
	ListNode *p;
	printf("*** The strings currently in our list are:\n");
	p=this->head;
	while(p!=NULL)
	{
	printf("%s\n",p->string);
	p=p->next;
	}
	}
	ListNode StringList::search(char string[1024])
	{
	// Find a node in the list that contains the requested
	// string. Return a *COPY* of the node that has no
	// pointers to list data. If no matching string is found,
	// it returns an <empty> ListNode.
	ListNode *p, copy;
	strcpy(&copy.string[0],"");
	copy.next=NULL;
	p=head;
	while (p!=NULL)
	{
	if (strcmp(string,p->string)==0)
	{
	copy=*(p);
	copy.next=NULL;
	return copy;
	}
	p=p->next;
	}
	return copy;
}
void StringList::clear_list(void)
{
	// Free all memory allocated to the linked list, reset
	// length to zero, and set head pointer to NULL
	while (this->head!=NULL)
	remove_head();
	}
	int StringList::get_length(void)
	{
	// This is what in object-oriented programming is called
	// a ’getter’. A function that returns the *value* of
	// a private variable so the user can find out what it is
	// without actually getting direct access to read or change
	// the variable.
	return this->list_length;
}
void StringList::remove_head(void)
{
	// Removes the node at the head of the linked list
	// and releases the memory allocated to the list
	// node. It reduces the length of the list by 1
	//
	// This function is used by the function that
	// clears the linked list. We do not give the users
	// of the class access to it because they could
	// use it to remove list data without
	// regard for the contents. Hence, we make this
	// function private.
	ListNode *p;
	if (this->head==NULL) return;
	p=this->head;
	this->head=this->head->next;
	delete p;
	this->list_length--;
}
```
### Header File
For header file: `Stringlist.h`
```h
class StringList{
	private:
		ListNode *head;
		int list_length;
		void remove_head(void);
	public:
		StringList(){
			head=NULL;
			list_length=0;	
		}
		~StringList(){
			clear_list();
		}
		void insert_string(char string[1024]);
		void delete_string(char string[1024]);
		void print_strings(void);
		ListNode search(char string[1024]);
		void clear_list();
		int get_length();
}
```