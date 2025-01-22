---
tags:
  - c
---
```c
int sum (int a, int b){
// declarations and statements if any
	return a+b;
}
```

Functions must be declared before they are used. or use [[C++ Forward Declaration]]
Every function will be allocated onto the [[Heap]]:
- A address space for every parameter (pointer or actual data)
- A address space for every variable
- An address space for the function
# Argument behavior
https://stackoverflow.com/questions/23480542/are-the-arguments-of-a-c-program-guaranteed-to-be-0-terminated
- Arguments are treated like a list
- In the memory, they will be null terminated 

# Default return type of 'int'
All c functions have an assumed return type of **int** unless you specify otherwise.
```c
myfuncion (){

}
```
# Return null
```c
int haha (){
	return; // return nothing at all
}
```

# void return
Sometimes you just dont intend to return at all. make the return type void then
```c
void manipulator(int &balls){
	(balls)++;
} 
```
# Return types are always typecasted
[[C Typecasting]]
```c
int dtoi(double mynum){
	return mynum;
}
```
They will typecast if the typecast makes sense

# Function impossibilities
- it is impossible for a function to take on infinite arguments. better to use a struct or array