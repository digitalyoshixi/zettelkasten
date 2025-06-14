---
tags:
  - go
---
A method to implement [[Concurrency]] or [[Paralellism]] in [[Go|Golang]].
Makes use of:
- [[Go Wait Group]]
- [[Go Channel Group]]
# Boilerplate
```go
func main(){
	var wg sync.WaitGroup
	
	wg.add(1)
	go func(){
		defer wg.Done() // when this function exits, set the waitgroup as done
		// body of function
	}()
	wg.Wait() // wait till all waitgroups are done
	fmt.Println("Done")	
}
```