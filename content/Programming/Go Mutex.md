---
tags:
  - programming
  - go
aliases:
  - Go sync
---
An implementation of [[Mutex]] in golang.
```go
package main

import (
	"fmt"
	"sync"
)

type Counter struct {
	mu sync.Mutex
	count int
}

func (c *Counter) Increment() {
	c.mu.Lock()
	// critical section code
	c.count++
	c.mu.Unlock()
}

func (c *Counter) GetCount() {
	c.mu.Lock()
	// critical section code
	defer c.mu.Unlock()
	return c.count
}

func main() {
	counter := &Counter{}
	
	var wg sync.WaitGroup
	
	for i := 0; i < 100; i ++ {
		wg.Add(1)
		
		go func() {
			counter.Increment()
			wg.Done()
		}
	}
	wg.Wait()
	
	fmt.Println("Final count:", counter.GetCount())
}
```