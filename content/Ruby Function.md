---
tags:
  - ruby
  - programming
aliases:
  - Ruby Method
---
# No Argument Function
```ruby
def myfunc
	puts "Hello"
end
# these two do the same thing
myfunc
myfunc()
```
# One Argument Function
```ruby
def myfunc2(name)
	puts "Hello #(name)"
end

myfunc2("DANIEL")
```
# Two Argument Function
```ruby
def myfunc2(name, age)
	puts "Hello #(name), aged #(age)"
end

myfunc2("DANIEL", 20)
```
# Default Parameter Function
```ruby
def myfunc2(name = "daniel", age = 12)
	puts "Hello #(name), aged #(age)"
end

myfunc2()
```