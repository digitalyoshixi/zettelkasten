---
tags:
  - go
  - programming
---
A library used for formatting output 
# `fmt.Print()`
Prints without newline
```go
fmt.Print("hello")
```
# `fmt.Println()`
Prints with newline
```go
fmt.Println("hello")
```
# `fmt.Printf()`
Prints with format specifiers:
- `%v` prints the value of the variable
- `%T` prints the type of the variable
```go
string mystrig = "yo";
fmt.Println("%v, %T", mystrig, mystrig);
```