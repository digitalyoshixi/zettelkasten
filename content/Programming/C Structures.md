---
tags:
  - c
aliases:
  - Struct
  - Compound Datatypes
  - CDT
  - Record
  - UDT
  - User Defined Datatype
---
A user defined datatype that allows you to combine several datatypes.
They are passed by value.
# Template
```c
struct structure_tag{
	datatype1 var1;
	datatype2 var2;
	...
	
} [define some structure variables(optional)];
```
### Example
```c
struct Book {
	char title[50];
	char author[50];
	char subject[50];
	int isbn;
};
int main(){
	struct Book mybook = {"THEGATPSY", "ME", "meta phyction"};
}
```
### Example 2
```c
struct Bone{
	int density;
	int weight;
} femur, tibia; // declare some global variables right away

int main(){
	femur.density = 20;
	tibia.weight = 40;
}
```
### Example 3
```c
struct Ball{
	int buoyancy;
	char type[10];
} soccer = {10,"soccer"}, basket = {50,"basket"}; // define the global variables

int main(){
	printf("%d",soccer.buoyancy);
}
```
### Throwaway structs
If your struct does not need to be used again, then you can make a struct with **NO** tag and then make some variables with it.
```c
struct {
	int bowelmovement;
	char name[20];
} daniel = {15,"daniel"};

int main(){
	printf("%s", daniel.name);
}
```

# Accessing Attributes
Simple do `variable.attributename`
you can set it to things, and read it directly
### Pointer Access Attributes
```c
// if you make a pointer, that pointer can access attributes easily.
struct Books{
	char title[50];
	char author[50];
}
int main(){
struct Books mybook = {"bangers", "me"};
struct Books *bookptr = &mybook; // make a pointer
printf("%s", bookptr->title);
printf("%s", bookptr->author);
}
```
# Packed Memory
The nature of structs insists that data is close close together.
If you require data to be packed very tightly, then consider putting them all in a struct.
Use this if you are:
- Packing several objects into a machine word
- Reading non-standard file formats outside of word length i.e 9-bit integers
```c
struct packed_struct {
   unsigned int f1:1;
   unsigned int f2:1;
   unsigned int f3:1;
   unsigned int f4:1;
   unsigned int type:4;
   unsigned int my_int:9;
}
```