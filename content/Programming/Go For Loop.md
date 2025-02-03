---
tags:
  - go
  - programming
---
# Classic For Loop
```go
for i:=0; i < 5; i++ {
	fmt.Println(i)
}
```
# For Loop In Range
Can iterate through an [[Go Arrays]], [[Go Slices]], [[Go Map]]
```
for _index, value :=_ range _array_|_slice_|_map_ {  
   _// code to be executed for each iteration_  
}
```
```go
fruits := [3]string{"apple", "orange", "banana"}  
for idx, val := range fruits {  
	fmt.Printf("%v\t%v\n", idx, val)  
}  
```