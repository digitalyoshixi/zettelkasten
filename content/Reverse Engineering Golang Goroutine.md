---
tags:
  - go
  - reverse_engineering
---
https://foxtrot-sq.medium.com/debugging-golang-based-elf-malware-7ec834f22607

Goroutines use [[Go Channels]] to communicate with eachother `make(chan val-type).`

When we define a goroutine like `go hello()`, the compiler turns it into a statement `runtime.newproc(size, hello, args)`.
The compiler will also add [[Golang Write Barrier]] for the garbage collector