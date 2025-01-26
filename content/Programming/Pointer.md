---
tags:
  - c
  - programming
  - memory
---
These are variables that store the address of another variable. 

They will be the same type as the data they are referencing. 

A special pointer is the [[Null Pointer]]
### Creating a pointer
```c
int x = 10;
int *mypointer = &x; // notice we are storing the address
int* mypointer2 = &x; //alternate way
```
### Reading pointers / Getting Address
```c
printf("%d",p); // reading address (in hex) 
printf("%p",p); // reading address (idk what this is in)
printf("%p",&*p); // reading address again haha
```
### Dereferencing / Getting value
Dereferencing is changing data of a variable by changing the pointer value. This changes the original variable data thus changing pointer data as well.
```c
printf("%d", *mypointer);
```
`*p` will get you the data of a pointer

You can have the same pointer variable and change the memory address, thereby reassigning the value of it. 
You cannot reassign variables that are not pointers to new memory addresses.

### Pointer Arithmetic
Arithmetic involving pointers will not directly modify to the expected result.
For example:
```c
int *ptr = NULL;
ptr++; // will actually increase by 4. int has 4bytes size
```
Instead, the value gained/lost will depend on the **datatype** that the pointer is,
### Pointer to Pointer
To have a pointer point to another pointer, you will use 2 asterisks. 
`int **q = &p.`
**This might seem useless, until you realize that you can use this method to effectively query down the initial data down to what you require with very minimal storage. Though, this is only possible with functions that modify multiple pointer behavior.**

### Pointer Function reference
Due to the local and global limitations of functions, you tend not to be able to modify a variable from functions outside of the function, however using pointers, you can reference the original variable from the address and modify it from there.

### [[Array Of Pointers]]

### Arrays as function arguments
```c
void addem (int *A){
	int valA = *A; // of course!
}
```
### Arrays as function returns
```c
int *retptr(){
	static int a = 20;
	return *a;  
} 
```
### Pointers and Matrixes

This one is really dang tough.

1. you will create your matrix as a double pointer. Int **p.
    
2. Malloc the data for the # of rows NOT the number of total data stored in array, just data for # of rows, eg. 4 integer rows is 4, 4 double rows is 16. p = (int\*\*)malloc(4)
    
3. For each row, malloc the data for the row. This allows you to have some rows with more slots than others. Tp[0] is row 0, p[0][0] is cell 0. So to malloc first row you would type: p[0] = (int *)malloc(3)
    

This explanation is very bad, but it will suffice for now.