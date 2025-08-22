---
tags:
  - ruby
  - programming
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
# Argument Function
```ruby
def myfunc2(name)
	puts "Hello #(name)"
end

myfunc2("DANIEL")
```