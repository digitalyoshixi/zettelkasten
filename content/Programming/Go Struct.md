---
tags:
  - go
  - programming
aliases:
  - Go Anonymous Struct
---
```go
type Person struct {
  name string
  age int
  job string
  salary int
}
```
# Accessing/Creating Members
```go
var pers1 Person  
pers1.name = "Hege"  
pers1.age = 45

var pers2 := Person{
	name: "Alice",
	age : 30
}
```
# Anonymous Structs
One time structs, never used again.
```go
job := struct {
	title string
	salary int
} { 
	title : "software engineer",
	salary : 200
}

fmt.Println(job.title)
```
# Struct Pointers
```go
employeePtr := &employee1
employeePtr.age
```