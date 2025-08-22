---
tags:
  - programming
  - ruby
---
A modifier that allows exposing attributes for objects to directly view/modify.
```ruby
class myClass
	attr_accessor : name
	def initialize(name)
		@name = name
end
```
This will expose the methods:
- `name` : returns the value of name
- `name=` : modify the value of name
```ruby
myObject = myclass.new("daniel")
myObject.name # will return 'daniel'
myObject.name="david" # will modify value
```