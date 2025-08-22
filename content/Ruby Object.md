---
tags:
  - programming
  - ruby
---
```ruby
class myClass
	def initialize(name = "Daniel")
		@name = name
	end
	
	def say_hi
		puts "Hi #(@name)"
	end
end

myObject = myClass.new("david")
myObject.say_hi
```
# Viewing Instance Methods
```ruby
myClass.instance_methods
```
![[Ruby Object-20250822164207344.webp]]
### Viewing Without Ancestors
```ruby
myClass.instance_methods(false)
```
![[Ruby Object-20250822164322904.webp]]