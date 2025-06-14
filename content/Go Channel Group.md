---
tags:
  - go
  - programming
---
This is a method for [[Interprocess Communication]] between a main thread and a goroutine.
# Example
```go
func main(){
	c := make(chan int)

	go func(){
		sum := 0
		c <- sum // send the sum to our channel
	}()
	output := <-c
	fmt.Println(output)
	
}
```