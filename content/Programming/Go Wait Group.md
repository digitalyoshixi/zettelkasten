---
tags:
  - go
  - programming
---
A group that exists to halt execution in a main go thread, until all waited processes signals done.
Required for concurrency in [[Goroutine]]
# Example
```go
var wg sync.WaitGroup

wg.Add(1)
go func(){
	defer wg.Done() // signal done after function exits
	fmt.Println("i am running")
}()
```